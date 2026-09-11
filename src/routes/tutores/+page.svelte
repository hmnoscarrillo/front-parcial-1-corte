<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import {
		tutoresAcademicosStore,
		tutoresEmpresarialesStore,
		empresasStore
	} from '$lib/data/mockData.js';

	let pestanaActiva = $state('academicos'); // 'academicos' | 'empresariales'
	let busqueda = $state('');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	// Modelo Tutor Académico
	let nuevoAcademico = $state({
		documento: '',
		nombres: '',
		apellidos: '',
		correo: '',
		telefono: '',
		departamento: 'Ingeniería de Software',
		especialidad: '',
		estado: 'Activo'
	});

	// Modelo Tutor Empresarial
	let nuevoEmpresarial = $state({
		documento: '',
		empresa_id: 1,
		nombres: '',
		apellidos: '',
		cargo: '',
		correo: '',
		telefono: '',
		estado: 'Activo'
	});

	let academicosFiltrados = $derived(
		$tutoresAcademicosStore.filter((t) => {
			const nombreCompleto = `${t.nombres} ${t.apellidos}`.toLowerCase();
			return (
				nombreCompleto.includes(busqueda.toLowerCase()) ||
				t.documento.includes(busqueda) ||
				t.departamento.toLowerCase().includes(busqueda.toLowerCase())
			);
		})
	);

	let empresarialesFiltrados = $derived(
		$tutoresEmpresarialesStore.filter((t) => {
			const nombreCompleto = `${t.nombres} ${t.apellidos}`.toLowerCase();
			return (
				nombreCompleto.includes(busqueda.toLowerCase()) ||
				t.empresa.toLowerCase().includes(busqueda.toLowerCase()) ||
				t.cargo.toLowerCase().includes(busqueda.toLowerCase())
			);
		})
	);

	function guardarTutor(event) {
		event.preventDefault();
		if (pestanaActiva === 'academicos') {
			const id = $tutoresAcademicosStore.length ? Math.max(...$tutoresAcademicosStore.map((t) => t.id)) + 1 : 1;
			tutoresAcademicosStore.update((lista) => [
				{ id, ...nuevoAcademico },
				...lista
			]);
			mensajeAlerta = `¡Tutor académico "${nuevoAcademico.nombres} ${nuevoAcademico.apellidos}" registrado con éxito!`;
			nuevoAcademico = {
				documento: '',
				nombres: '',
				apellidos: '',
				correo: '',
				telefono: '',
				departamento: 'Ingeniería de Software',
				especialidad: '',
				estado: 'Activo'
			};
		} else {
			const emp = $empresasStore.find((e) => e.id === Number(nuevoEmpresarial.empresa_id));
			const nombreEmpresa = emp ? emp.razon_social : 'TechInnovate Solutions S.A.S.';
			const id = $tutoresEmpresarialesStore.length ? Math.max(...$tutoresEmpresarialesStore.map((t) => t.id)) + 1 : 1;
			tutoresEmpresarialesStore.update((lista) => [
				{ id, ...nuevoEmpresarial, empresa: nombreEmpresa },
				...lista
			]);
			mensajeAlerta = `¡Tutor empresarial "${nuevoEmpresarial.nombres} ${nuevoEmpresarial.apellidos}" registrado con éxito!`;
			nuevoEmpresarial = {
				documento: '',
				empresa_id: 1,
				nombres: '',
				apellidos: '',
				cargo: '',
				correo: '',
				telefono: '',
				estado: 'Activo'
			};
		}
		mostrarFormulario = false;
	}

	function eliminarAcademico(id, nombre) {
		if (confirm(`¿Eliminar tutor académico "${nombre}"?`)) {
			tutoresAcademicosStore.update((l) => l.filter((x) => x.id !== id));
			mensajeAlerta = `Tutor "${nombre}" retirado.`;
		}
	}

	function eliminarEmpresarial(id, nombre) {
		if (confirm(`¿Eliminar tutor empresarial "${nombre}"?`)) {
			tutoresEmpresarialesStore.update((l) => l.filter((x) => x.id !== id));
			mensajeAlerta = `Tutor "${nombre}" retirado.`;
		}
	}
</script>

<svelte:head>
	<title>Tutores Académicos y Empresariales | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Tutores', href: '/tutores' }]} />

	<!-- Encabezado -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<h2 class="h3 fw-bold text-dark mb-1">
				<i class="bi bi-person-badge text-primary me-2"></i>Gestión de Tutores y Asesores
			</h2>
			<p class="text-muted mb-0 small">
				Supervisión dual: Asesores Académicos (Universidad) y Mentores Empresariales (Empresas Aliadas).
			</p>
		</div>
		<button
			type="button"
			class="btn btn-primary d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-plus-circle-fill'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : pestanaActiva === 'academicos' ? 'Nuevo Tutor Académico' : 'Nuevo Tutor Empresarial'}</span>
		</button>
	</header>

	{#if mensajeAlerta}
		<div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
			<i class="bi bi-check-circle-fill me-2"></i>{mensajeAlerta}
			<button type="button" class="btn-close" onclick={() => (mensajeAlerta = '')} aria-label="Cerrar"></button>
		</div>
	{/if}

	<!-- Pestañas de Navegación Dual -->
	<ul class="nav nav-pills mb-4 bg-white p-2 rounded-3 shadow-sm border">
		<li class="nav-item">
			<button
				type="button"
				class="nav-link fw-bold d-flex align-items-center gap-2 {pestanaActiva === 'academicos' ? 'active shadow-sm' : 'text-secondary'}"
				onclick={() => { pestanaActiva = 'academicos'; mostrarFormulario = false; }}
			>
				<i class="bi bi-mortarboard-fill"></i>
				<span>Tutores Académicos (Docentes)</span>
				<span class="badge bg-white text-dark ms-1">{$tutoresAcademicosStore.length}</span>
			</button>
		</li>
		<li class="nav-item">
			<button
				type="button"
				class="nav-link fw-bold d-flex align-items-center gap-2 {pestanaActiva === 'empresariales' ? 'active shadow-sm' : 'text-secondary'}"
				onclick={() => { pestanaActiva = 'empresariales'; mostrarFormulario = false; }}
			>
				<i class="bi bi-building"></i>
				<span>Tutores Empresariales (Mentores)</span>
				<span class="badge bg-white text-dark ms-1">{$tutoresEmpresarialesStore.length}</span>
			</button>
		</li>
	</ul>

	<!-- Formulario de Registro Dinámico -->
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-primary">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-primary">
					<i class="bi bi-person-plus-fill me-2"></i>
					{pestanaActiva === 'academicos' ? 'Ficha de Tutor Académico (Docente)' : 'Ficha de Tutor Empresarial (Mentor de Empresa)'}
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={guardarTutor}>
					<div class="row g-3">
						<div class="col-12 col-md-3">
							<label for="docTutor" class="form-label fw-semibold small">No. Documento *</label>
							{#if pestanaActiva === 'academicos'}
								<input id="docTutor" type="text" class="form-control" placeholder="79845123" required bind:value={nuevoAcademico.documento} />
							{:else}
								<input id="docTutor" type="text" class="form-control" placeholder="19876543" required bind:value={nuevoEmpresarial.documento} />
							{/if}
						</div>
						<div class="col-12 col-md-4">
							<label for="nomTutor" class="form-label fw-semibold small">Nombres *</label>
							{#if pestanaActiva === 'academicos'}
								<input id="nomTutor" type="text" class="form-control" placeholder="Fernando" required bind:value={nuevoAcademico.nombres} />
							{:else}
								<input id="nomTutor" type="text" class="form-control" placeholder="Andrea" required bind:value={nuevoEmpresarial.nombres} />
							{/if}
						</div>
						<div class="col-12 col-md-5">
							<label for="apeTutor" class="form-label fw-semibold small">Apellidos *</label>
							{#if pestanaActiva === 'academicos'}
								<input id="apeTutor" type="text" class="form-control" placeholder="Jaramillo Restrepo" required bind:value={nuevoAcademico.apellidos} />
							{:else}
								<input id="apeTutor" type="text" class="form-control" placeholder="Salazar Marín" required bind:value={nuevoEmpresarial.apellidos} />
							{/if}
						</div>

						{#if pestanaActiva === 'academicos'}
							<div class="col-12 col-md-4">
								<label for="depTutor" class="form-label fw-semibold small">Departamento / Área *</label>
								<input id="depTutor" type="text" class="form-control" placeholder="Ingeniería de Software" required bind:value={nuevoAcademico.departamento} />
							</div>
							<div class="col-12 col-md-4">
								<label for="espTutor" class="form-label fw-semibold small">Especialidad Académica *</label>
								<input id="espTutor" type="text" class="form-control" placeholder="Arquitectura Cloud, DevOps" required bind:value={nuevoAcademico.especialidad} />
							</div>
						{:else}
							<div class="col-12 col-md-4">
								<label for="empTutor" class="form-label fw-semibold small">Empresa Vinculada *</label>
								<select id="empTutor" class="form-select" bind:value={nuevoEmpresarial.empresa_id} required>
									{#each $empresasStore as emp}
										<option value={emp.id}>{emp.razon_social}</option>
									{/each}
								</select>
							</div>
							<div class="col-12 col-md-4">
								<label for="cargTutor" class="form-label fw-semibold small">Cargo en la Empresa *</label>
								<input id="cargTutor" type="text" class="form-control" placeholder="Tech Lead / Gerente TI" required bind:value={nuevoEmpresarial.cargo} />
							</div>
						{/if}

						<div class="col-12 col-md-4">
							<label for="corTutor" class="form-label fw-semibold small">Correo Electrónico *</label>
							{#if pestanaActiva === 'academicos'}
								<input id="corTutor" type="email" class="form-control" placeholder="docente@universidad.edu.co" required bind:value={nuevoAcademico.correo} />
							{:else}
								<input id="corTutor" type="email" class="form-control" placeholder="tutor@empresa.com" required bind:value={nuevoEmpresarial.correo} />
							{/if}
						</div>
						<div class="col-12 col-md-4">
							<label for="telTutor" class="form-label fw-semibold small">Teléfono / Celular *</label>
							{#if pestanaActiva === 'academicos'}
								<input id="telTutor" type="tel" class="form-control" placeholder="3128901234" required bind:value={nuevoAcademico.telefono} />
							{:else}
								<input id="telTutor" type="tel" class="form-control" placeholder="3001234567" required bind:value={nuevoEmpresarial.telefono} />
							{/if}
						</div>
						<div class="col-12 col-md-4 d-flex align-items-end">
							<button type="submit" class="btn btn-success w-100 fw-bold shadow-sm">
								<i class="bi bi-check2-circle me-1"></i>Guardar Tutor
							</button>
						</div>
					</div>
				</form>
			</div>
		</section>
	{/if}

	<!-- Búsqueda -->
	<section class="card border-0 shadow-sm rounded-3 mb-4">
		<div class="card-body p-3">
			<div class="input-group">
				<span class="input-group-text bg-light border-end-0">
					<i class="bi bi-search text-muted"></i>
				</span>
				<input
					type="search"
					class="form-control border-start-0"
					placeholder="Buscar tutor por nombre, documento, empresa o especialidad..."
					bind:value={busqueda}
				/>
			</div>
		</div>
	</section>

	<!-- Tabla según Pestaña Activa -->
	{#if pestanaActiva === 'academicos'}
		<section class="card border-0 shadow-sm rounded-3">
			<div class="card-body p-0">
				<div class="table-responsive">
					<table class="table table-hover align-middle mb-0">
						<thead class="table-light text-uppercase small text-muted">
							<tr>
								<th class="ps-4">Documento</th>
								<th>Nombre del Docente</th>
								<th>Departamento</th>
								<th>Especialidad</th>
								<th>Contacto</th>
								<th>Estado</th>
								<th class="text-end pe-4">Acciones</th>
							</tr>
						</thead>
						<tbody>
							{#if academicosFiltrados.length === 0}
								<tr>
									<td colspan="7" class="text-center py-4 text-muted">No se encontraron tutores académicos.</td>
								</tr>
							{:else}
								{#each academicosFiltrados as a}
									<tr>
										<td class="ps-4 font-monospace text-muted small">{a.documento}</td>
										<td>
											<div class="fw-bold text-dark">{a.nombres} {a.apellidos}</div>
										</td>
										<td>
											<span class="badge bg-light text-dark border">{a.departamento}</span>
										</td>
										<td>
											<small class="text-secondary">{a.especialidad}</small>
										</td>
										<td>
											<div class="small"><i class="bi bi-envelope me-1"></i>{a.correo}</div>
											<div class="small text-muted"><i class="bi bi-telephone me-1"></i>{a.telefono}</div>
										</td>
										<td>
											<span class="badge bg-success-subtle text-success border border-success-subtle">{a.estado}</span>
										</td>
										<td class="text-end pe-4">
											<button type="button" class="btn btn-sm btn-outline-danger" aria-label={'Eliminar tutor ' + a.nombres + ' ' + a.apellidos} title="Eliminar tutor" onclick={() => eliminarAcademico(a.id, `${a.nombres} ${a.apellidos}`)}>
												<i class="bi bi-trash"></i>
											</button>
										</td>
									</tr>
								{/each}
							{/if}
						</tbody>
					</table>
				</div>
			</div>
		</section>
	{:else}
		<section class="card border-0 shadow-sm rounded-3">
			<div class="card-body p-0">
				<div class="table-responsive">
					<table class="table table-hover align-middle mb-0">
						<thead class="table-light text-uppercase small text-muted">
							<tr>
								<th class="ps-4">Documento</th>
								<th>Nombre del Mentor</th>
								<th>Empresa Aliada</th>
								<th>Cargo</th>
								<th>Contacto</th>
								<th>Estado</th>
								<th class="text-end pe-4">Acciones</th>
							</tr>
						</thead>
						<tbody>
							{#if empresarialesFiltrados.length === 0}
								<tr>
									<td colspan="7" class="text-center py-4 text-muted">No se encontraron tutores empresariales.</td>
								</tr>
							{:else}
								{#each empresarialesFiltrados as e}
									<tr>
										<td class="ps-4 font-monospace text-muted small">{e.documento}</td>
										<td>
											<div class="fw-bold text-dark">{e.nombres} {e.apellidos}</div>
										</td>
										<td>
											<span class="badge bg-info-subtle text-info border border-info-subtle">{e.empresa}</span>
										</td>
										<td>
											<small class="text-secondary">{e.cargo}</small>
										</td>
										<td>
											<div class="small"><i class="bi bi-envelope me-1"></i>{e.correo}</div>
											<div class="small text-muted"><i class="bi bi-telephone me-1"></i>{e.telefono}</div>
										</td>
										<td>
											<span class="badge bg-success-subtle text-success border border-success-subtle">{e.estado}</span>
										</td>
										<td class="text-end pe-4">
											<button type="button" class="btn btn-sm btn-outline-danger" aria-label={'Eliminar tutor ' + e.nombres + ' ' + e.apellidos} title="Eliminar tutor" onclick={() => eliminarEmpresarial(e.id, `${e.nombres} ${e.apellidos}`)}>
												<i class="bi bi-trash"></i>
											</button>
										</td>
									</tr>
								{/each}
							{/if}
						</tbody>
					</table>
				</div>
			</div>
		</section>
	{/if}
</div>
