<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import { estudiantesStore, programasStore } from '$lib/data/mockData.js';

	let busqueda = $state('');
	let filtroPrograma = $state('todos');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	let nuevoEstudiante = $state({
		tipo_doc: 'CC',
		documento: '',
		nombres: '',
		apellidos: '',
		correo: '',
		telefono: '',
		programa_id: 1,
		semestre: 9,
		promedio: 4.2,
		estado: 'Activo'
	});

	let estudiantesFiltrados = $derived(
		$estudiantesStore.filter((est) => {
			const nombreCompleto = `${est.nombres} ${est.apellidos}`.toLowerCase();
			const matchTexto =
				nombreCompleto.includes(busqueda.toLowerCase()) ||
				est.documento.includes(busqueda) ||
				est.correo.toLowerCase().includes(busqueda.toLowerCase());
			const matchPrograma =
				filtroPrograma === 'todos' || est.programa === filtroPrograma;
			return matchTexto && matchPrograma;
		})
	);

	function registrarEstudiante(event) {
		event.preventDefault();
		const prog = $programasStore.find((p) => p.id === Number(nuevoEstudiante.programa_id));
		const nombrePrograma = prog ? prog.nombre : 'Ingeniería de Sistemas';

		const id = $estudiantesStore.length ? Math.max(...$estudiantesStore.map((e) => e.id)) + 1 : 1;
		estudiantesStore.update((lista) => [
			{
				id,
				...nuevoEstudiante,
				programa: nombrePrograma
			},
			...lista
		]);

		mensajeAlerta = `¡Estudiante "${nuevoEstudiante.nombres} ${nuevoEstudiante.apellidos}" registrado exitosamente!`;
		nuevoEstudiante = {
			tipo_doc: 'CC',
			documento: '',
			nombres: '',
			apellidos: '',
			correo: '',
			telefono: '',
			programa_id: 1,
			semestre: 9,
			promedio: 4.2,
			estado: 'Activo'
		};
		mostrarFormulario = false;
	}

	function eliminarEstudiante(id, nombre) {
		if (confirm(`¿Está seguro de dar de baja al estudiante "${nombre}"?`)) {
			estudiantesStore.update((lista) => lista.filter((e) => e.id !== id));
			mensajeAlerta = `Estudiante "${nombre}" eliminado del directorio.`;
		}
	}
</script>

<svelte:head>
	<title>Estudiantes en Práctica | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Estudiantes', href: '/estudiantes' }]} />

	<!-- Encabezado -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<h2 class="h3 fw-bold text-dark mb-1">
				<i class="bi bi-people-fill text-success me-2"></i>Directorio de Estudiantes Habilitados
			</h2>
			<p class="text-muted mb-0 small">
				Registro académico de aspirantes y practicantes con validación de requisitos curriculares.
			</p>
		</div>
		<button
			type="button"
			class="btn btn-success text-white fw-bold d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-person-plus-fill'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : 'Nuevo Estudiante'}</span>
		</button>
	</header>

	{#if mensajeAlerta}
		<div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
			<i class="bi bi-check-circle-fill me-2"></i>{mensajeAlerta}
			<button type="button" class="btn-close" onclick={() => (mensajeAlerta = '')} aria-label="Cerrar"></button>
		</div>
	{/if}

	<!-- Formulario de Registro -->
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-success">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-success">
					<i class="bi bi-person-badge-fill me-2"></i>Ficha de Inscripción de Estudiante
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={registrarEstudiante}>
					<div class="row g-3">
						<div class="col-12 col-md-2">
							<label for="tipo_doc" class="form-label fw-semibold small">Tipo Doc *</label>
							<select id="tipo_doc" class="form-select" bind:value={nuevoEstudiante.tipo_doc} required>
								<option value="CC">Cédula (CC)</option>
								<option value="TI">Tarjeta Identidad (TI)</option>
								<option value="CE">Cédula Extranjería (CE)</option>
								<option value="PAS">Pasaporte</option>
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="documento" class="form-label fw-semibold small">No. Documento *</label>
							<input id="documento" type="text" class="form-control" placeholder="1018456789" required bind:value={nuevoEstudiante.documento} />
						</div>
						<div class="col-12 col-md-3">
							<label for="nombres" class="form-label fw-semibold small">Nombres *</label>
							<input id="nombres" type="text" class="form-control" placeholder="Mateo Alejandro" required bind:value={nuevoEstudiante.nombres} />
						</div>
						<div class="col-12 col-md-4">
							<label for="apellidos" class="form-label fw-semibold small">Apellidos *</label>
							<input id="apellidos" type="text" class="form-control" placeholder="Pérez Suárez" required bind:value={nuevoEstudiante.apellidos} />
						</div>
						<div class="col-12 col-md-4">
							<label for="correo" class="form-label fw-semibold small">Correo Institucional *</label>
							<input id="correo" type="email" class="form-control" placeholder="estudiante@universidad.edu.co" required bind:value={nuevoEstudiante.correo} />
						</div>
						<div class="col-12 col-md-3">
							<label for="telefono" class="form-label fw-semibold small">Teléfono / Celular *</label>
							<input id="telefono" type="tel" class="form-control" placeholder="3104567890" required bind:value={nuevoEstudiante.telefono} />
						</div>
						<div class="col-12 col-md-5">
							<label for="programa_id" class="form-label fw-semibold small">Programa Académico *</label>
							<select id="programa_id" class="form-select" bind:value={nuevoEstudiante.programa_id} required>
								{#each $programasStore as prog}
									<option value={prog.id}>{prog.nombre} ({prog.codigo})</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="semestre" class="form-label fw-semibold small">Semestre Actual *</label>
							<select id="semestre" class="form-select" bind:value={nuevoEstudiante.semestre} required>
								<option value={7}>Semestre 7</option>
								<option value={8}>Semestre 8</option>
								<option value={9}>Semestre 9</option>
								<option value={10}>Semestre 10</option>
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="promedio" class="form-label fw-semibold small">Promedio Acumulado *</label>
							<input id="promedio" type="number" step="0.1" min="3.0" max="5.0" class="form-control" required bind:value={nuevoEstudiante.promedio} />
						</div>
						<div class="col-12 col-md-3">
							<label for="estadoEst" class="form-label fw-semibold small">Estado Inicial *</label>
							<select id="estadoEst" class="form-select" bind:value={nuevoEstudiante.estado} required>
								<option value="Activo">Activo</option>
								<option value="Inactivo">Inactivo</option>
							</select>
						</div>
						<div class="col-12 col-md-3 d-flex align-items-end">
							<button type="submit" class="btn btn-success w-100 fw-bold shadow-sm">
								<i class="bi bi-person-check-fill me-1"></i>Guardar Estudiante
							</button>
						</div>
					</div>
				</form>
			</div>
		</section>
	{/if}

	<!-- Filtros y Búsqueda -->
	<section class="card border-0 shadow-sm rounded-3 mb-4">
		<div class="card-body p-3">
			<div class="row g-3 align-items-center">
				<div class="col-12 col-md-6">
					<div class="input-group">
						<span class="input-group-text bg-light border-end-0">
							<i class="bi bi-search text-muted"></i>
						</span>
						<input
							type="search"
							class="form-control border-start-0"
							placeholder="Buscar por documento, nombre o correo..."
							bind:value={busqueda}
						/>
					</div>
				</div>
				<div class="col-12 col-md-4">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroProg" class="text-nowrap small fw-semibold text-muted mb-0">Carrera:</label>
						<select id="filtroProg" class="form-select form-select-sm" bind:value={filtroPrograma}>
							<option value="todos">Todos los Programas</option>
							{#each $programasStore as prog}
								<option value={prog.nombre}>{prog.nombre}</option>
							{/each}
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2 text-md-end">
					<span class="badge bg-light text-secondary border px-3 py-2">
						{estudiantesFiltrados.length} Estudiantes
					</span>
				</div>
			</div>
		</div>
	</section>

	<!-- Tabla de Estudiantes -->
	<section class="card border-0 shadow-sm rounded-3">
		<div class="card-body p-0">
			<div class="table-responsive">
				<table class="table table-hover align-middle mb-0">
					<thead class="table-light text-uppercase small text-muted">
						<tr>
							<th class="ps-4">Documento</th>
							<th>Nombres y Apellidos</th>
							<th>Programa Académico</th>
							<th>Semestre</th>
							<th>Promedio</th>
							<th>Estado</th>
							<th class="text-end pe-4">Acciones</th>
						</tr>
					</thead>
					<tbody>
						{#if estudiantesFiltrados.length === 0}
							<tr>
								<td colspan="7" class="text-center py-4 text-muted">
									<i class="bi bi-people fs-3 d-block mb-1"></i>
									No hay estudiantes que coincidan con la búsqueda.
								</td>
							</tr>
						{:else}
							{#each estudiantesFiltrados as est}
								<tr>
									<td class="ps-4">
										<span class="font-monospace text-muted small">{est.tipo_doc}: {est.documento}</span>
									</td>
									<td>
										<div class="fw-bold text-dark">{est.nombres} {est.apellidos}</div>
										<small class="text-muted"><i class="bi bi-envelope me-1"></i>{est.correo}</small>
									</td>
									<td>
										<span class="fw-medium text-secondary">{est.programa}</span>
									</td>
									<td>
										<span class="badge bg-light text-dark border">Semestre {est.semestre}</span>
									</td>
									<td>
										<span class="badge {est.promedio >= 4.0 ? 'bg-success-subtle text-success' : 'bg-warning-subtle text-warning'} border">
											{est.promedio}
										</span>
									</td>
									<td>
										<span class="badge {est.estado === 'Activo' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-secondary'}">
											{est.estado}
										</span>
									</td>
									<td class="text-end pe-4">
										<button
											type="button"
											class="btn btn-sm btn-outline-danger"
											onclick={() => eliminarEstudiante(est.id, `${est.nombres} ${est.apellidos}`)}
											title="Eliminar Estudiante"
										>
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
</div>
