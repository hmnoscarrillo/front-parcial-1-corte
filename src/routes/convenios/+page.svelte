<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import { conveniosStore, empresasStore } from '$lib/data/mockData.js';

	let busqueda = $state('');
	let filtroEstado = $state('todos');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	let nuevoConvenio = $state({
		codigo: '',
		empresa_id: 1,
		tipo: 'Convenio Marco de Cooperación',
		fecha_inicio: '2026-03-01',
		fecha_fin: '2027-02-28',
		cupos_totales: 6,
		cupos_disponibles: 6,
		estado: 'Vigente'
	});

	let conveniosFiltrados = $derived(
		$conveniosStore.filter((c) => {
			const matchTexto =
				c.codigo.toLowerCase().includes(busqueda.toLowerCase()) ||
				c.empresa.toLowerCase().includes(busqueda.toLowerCase()) ||
				c.tipo.toLowerCase().includes(busqueda.toLowerCase());
			const matchEstado = filtroEstado === 'todos' || c.estado === filtroEstado;
			return matchTexto && matchEstado;
		})
	);

	function registrarConvenio(event) {
		event.preventDefault();
		const emp = $empresasStore.find((e) => e.id === Number(nuevoConvenio.empresa_id));
		const nombreEmpresa = emp ? emp.razon_social : 'TechInnovate Solutions S.A.S.';

		const id = $conveniosStore.length ? Math.max(...$conveniosStore.map((c) => c.id)) + 1 : 1;
		conveniosStore.update((lista) => [
			{ id, ...nuevoConvenio, empresa: nombreEmpresa },
			...lista
		]);

		mensajeAlerta = `¡Convenio "${nuevoConvenio.codigo}" registrado exitosamente con ${nombreEmpresa}!`;
		nuevoConvenio = {
			codigo: '',
			empresa_id: 1,
			tipo: 'Convenio Marco de Cooperación',
			fecha_inicio: '2026-03-01',
			fecha_fin: '2027-02-28',
			cupos_totales: 6,
			cupos_disponibles: 6,
			estado: 'Vigente'
		};
		mostrarFormulario = false;
	}

	function eliminarConvenio(id, codigo) {
		if (confirm(`¿Está seguro de eliminar el convenio "${codigo}"?`)) {
			conveniosStore.update((l) => l.filter((c) => c.id !== id));
			mensajeAlerta = `Convenio "${codigo}" eliminado.`;
		}
	}
</script>

<svelte:head>
	<title>Convenios Institucionales | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Convenios Institucionales', href: '/convenios' }]} />

	<!-- Encabezado -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<h2 class="h3 fw-bold text-dark mb-1">
				<i class="bi bi-file-earmark-text-fill text-warning me-2"></i>Gestión de Convenios Institucionales
			</h2>
			<p class="text-muted mb-0 small">
				Acuerdos formales de cooperación académica y empresarial que amparan legalmente las prácticas profesionales.
			</p>
		</div>
		<button
			type="button"
			class="btn btn-warning text-dark fw-bold d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-file-earmark-plus-fill'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : 'Nuevo Convenio'}</span>
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
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-warning">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-dark">
					<i class="bi bi-folder-plus text-warning me-2"></i>Apertura de Nuevo Convenio
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={registrarConvenio}>
					<div class="row g-3">
						<div class="col-12 col-md-3">
							<label for="codigoConv" class="form-label fw-semibold small">Código del Convenio *</label>
							<input id="codigoConv" type="text" class="form-control" placeholder="Ej: CONV-2026-004" required bind:value={nuevoConvenio.codigo} />
						</div>
						<div class="col-12 col-md-5">
							<label for="empresaConv" class="form-label fw-semibold small">Empresa Contraparte *</label>
							<select id="empresaConv" class="form-select" bind:value={nuevoConvenio.empresa_id} required>
								{#each $empresasStore as emp}
									<option value={emp.id}>{emp.razon_social} (NIT: {emp.nit})</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-4">
							<label for="tipoConv" class="form-label fw-semibold small">Modalidad / Tipo *</label>
							<select id="tipoConv" class="form-select" bind:value={nuevoConvenio.tipo} required>
								<option value="Convenio Marco de Cooperación">Convenio Marco de Cooperación</option>
								<option value="Convenio Específico de Prácticas">Convenio Específico de Prácticas</option>
								<option value="Convenio de Pasantía Investigativa">Convenio de Pasantía Investigativa</option>
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="fInicio" class="form-label fw-semibold small">Fecha de Inicio *</label>
							<input id="fInicio" type="date" class="form-control" required bind:value={nuevoConvenio.fecha_inicio} />
						</div>
						<div class="col-12 col-md-3">
							<label for="fFin" class="form-label fw-semibold small">Fecha de Vencimiento *</label>
							<input id="fFin" type="date" class="form-control" required bind:value={nuevoConvenio.fecha_fin} />
						</div>
						<div class="col-12 col-md-2">
							<label for="cuposTot" class="form-label fw-semibold small">Cupos Totales *</label>
							<input id="cuposTot" type="number" min="1" max="50" class="form-control" required bind:value={nuevoConvenio.cupos_totales} />
						</div>
						<div class="col-12 col-md-2">
							<label for="cuposDisp" class="form-label fw-semibold small">Cupos Libres *</label>
							<input id="cuposDisp" type="number" min="0" max="50" class="form-control" required bind:value={nuevoConvenio.cupos_disponibles} />
						</div>
						<div class="col-12 col-md-2">
							<label for="estConv" class="form-label fw-semibold small">Estado Legal *</label>
							<select id="estConv" class="form-select" bind:value={nuevoConvenio.estado} required>
								<option value="Vigente">Vigente</option>
								<option value="Próximo a Vencer">Próximo a Vencer</option>
								<option value="Vencido">Vencido</option>
							</select>
						</div>
						<div class="col-12 d-flex justify-content-end">
							<button type="submit" class="btn btn-success fw-bold px-4 shadow-sm">
								<i class="bi bi-check-circle-fill me-1"></i>Formalizar Convenio
							</button>
						</div>
					</div>
				</form>
			</div>
		</section>
	{/if}

	<!-- Filtros -->
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
							placeholder="Buscar por código, empresa o tipo de convenio..."
							bind:value={busqueda}
						/>
					</div>
				</div>
				<div class="col-12 col-md-4">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroEstConv" class="text-nowrap small fw-semibold text-muted mb-0">Estado:</label>
						<select id="filtroEstConv" class="form-select form-select-sm" bind:value={filtroEstado}>
							<option value="todos">Todos los Estados</option>
							<option value="Vigente">Vigente</option>
							<option value="Próximo a Vencer">Próximo a Vencer</option>
							<option value="Vencido">Vencido</option>
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2 text-md-end">
					<span class="badge bg-light text-secondary border px-3 py-2">
						{conveniosFiltrados.length} Convenios
					</span>
				</div>
			</div>
		</div>
	</section>

	<!-- Tabla de Convenios -->
	<section class="card border-0 shadow-sm rounded-3">
		<div class="card-body p-0">
			<div class="table-responsive">
				<table class="table table-hover align-middle mb-0">
					<thead class="table-light text-uppercase small text-muted">
						<tr>
							<th class="ps-4">Código</th>
							<th>Empresa Aliada</th>
							<th>Modalidad</th>
							<th>Vigencia</th>
							<th>Cupos Disponibles</th>
							<th>Estado</th>
							<th class="text-end pe-4">Acciones</th>
						</tr>
					</thead>
					<tbody>
						{#if conveniosFiltrados.length === 0}
							<tr>
								<td colspan="7" class="text-center py-4 text-muted">No se encontraron convenios.</td>
							</tr>
						{:else}
							{#each conveniosFiltrados as c}
								<tr>
									<td class="ps-4 font-monospace text-primary fw-bold">{c.codigo}</td>
									<td>
										<div class="fw-bold text-dark">{c.empresa}</div>
									</td>
									<td>
										<span class="badge bg-light text-dark border">{c.tipo}</span>
									</td>
									<td>
										<div class="small text-muted">
											<i class="bi bi-calendar-range me-1"></i>{c.fecha_inicio} al {c.fecha_fin}
										</div>
									</td>
									<td>
										<div class="d-flex align-items-center gap-2">
											<span class="fw-bold text-dark">{c.cupos_disponibles} de {c.cupos_totales}</span>
											<span class="badge bg-info-subtle text-info">Libres</span>
										</div>
									</td>
									<td>
										{#if c.estado === 'Vigente'}
											<span class="badge bg-success-subtle text-success border border-success-subtle">{c.estado}</span>
										{:else if c.estado === 'Próximo a Vencer'}
											<span class="badge bg-warning-subtle text-warning border border-warning-subtle">{c.estado}</span>
										{:else}
											<span class="badge bg-danger-subtle text-danger border border-danger-subtle">{c.estado}</span>
										{/if}
									</td>
									<td class="text-end pe-4">
							<button type="button" class="btn btn-sm btn-outline-danger" aria-label={'Eliminar convenio ' + c.codigo} title="Eliminar convenio" onclick={() => eliminarConvenio(c.id, c.codigo)}>
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
