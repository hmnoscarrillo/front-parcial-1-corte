<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import { programasStore } from '$lib/data/mockData.js';

	// Estado local para búsqueda y formulario
	let busqueda = $state('');
	let filtroFacultad = $state('todas');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	// Modelo del formulario
	let nuevoPrograma = $state({
		codigo: '',
		nombre: '',
		facultad: 'Facultad de Ingeniería',
		nivel: 'Pregrado',
		creditos: 160,
		estado: 'Activo'
	});

	// Programas filtrados
	let programasFiltrados = $derived(
		$programasStore.filter((p) => {
			const coincideBusqueda =
				p.nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
				p.codigo.toLowerCase().includes(busqueda.toLowerCase());
			const coincideFacultad =
				filtroFacultad === 'todas' || p.facultad === filtroFacultad;
			return coincideBusqueda && coincideFacultad;
		})
	);

	function guardarPrograma(event) {
		event.preventDefault();
		const id = $programasStore.length ? Math.max(...$programasStore.map((p) => p.id)) + 1 : 1;
		programasStore.update((lista) => [
			{ id, ...nuevoPrograma },
			...lista
		]);

		mensajeAlerta = `¡Programa "${nuevoPrograma.nombre}" registrado exitosamente en el sistema!`;
		// Reset form
		nuevoPrograma = {
			codigo: '',
			nombre: '',
			facultad: 'Facultad de Ingeniería',
			nivel: 'Pregrado',
			creditos: 160,
			estado: 'Activo'
		};
		mostrarFormulario = false;
	}

	function eliminarPrograma(id, nombre) {
		if (confirm(`¿Está seguro de eliminar el programa "${nombre}"?`)) {
			programasStore.update((lista) => lista.filter((p) => p.id !== id));
			mensajeAlerta = `Programa "${nombre}" eliminado correctamente.`;
		}
	}
</script>

<svelte:head>
	<title>Programas Académicos | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Programas Académicos', href: '/programas' }]} />

	<!-- Encabezado de Página -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<h2 class="h3 fw-bold text-dark mb-1">
				<i class="bi bi-mortarboard-fill text-primary me-2"></i>Gestión de Programas Académicos
			</h2>
			<p class="text-muted mb-0 small">
				Administración de carreras profesionales, facultades y créditos curriculares para prácticas.
			</p>
		</div>
		<button
			type="button"
			class="btn btn-primary d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-plus-circle-fill'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : 'Nuevo Programa'}</span>
		</button>
	</header>

	<!-- Mensaje de Feedback -->
	{#if mensajeAlerta}
		<div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
			<i class="bi bi-check-circle-fill me-2"></i>{mensajeAlerta}
			<button type="button" class="btn-close" onclick={() => (mensajeAlerta = '')} aria-label="Cerrar"></button>
		</div>
	{/if}

	<!-- Formulario de Registro (Colapsable) -->
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-primary">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-primary">
					<i class="bi bi-pencil-square me-2"></i>Registrar Nuevo Programa Académico
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={guardarPrograma}>
					<div class="row g-3">
						<div class="col-12 col-md-3">
							<label for="codigo" class="form-label fw-semibold small">Código del Programa *</label>
							<input
								id="codigo"
								type="text"
								class="form-control"
								placeholder="Ej: ING-SIS"
								required
								bind:value={nuevoPrograma.codigo}
							/>
						</div>
						<div class="col-12 col-md-5">
							<label for="nombre" class="form-label fw-semibold small">Nombre del Programa *</label>
							<input
								id="nombre"
								type="text"
								class="form-control"
								placeholder="Ej: Ingeniería de Sistemas"
								required
								bind:value={nuevoPrograma.nombre}
							/>
						</div>
						<div class="col-12 col-md-4">
							<label for="facultad" class="form-label fw-semibold small">Facultad *</label>
							<select id="facultad" class="form-select" bind:value={nuevoPrograma.facultad} required>
								<option value="Facultad de Ingeniería">Facultad de Ingeniería</option>
								<option value="Facultad de Ciencias Económicas">Facultad de Ciencias Económicas</option>
								<option value="Facultad de Artes y Diseño">Facultad de Artes y Diseño</option>
								<option value="Facultad de Ciencias Jurídicas">Facultad de Ciencias Jurídicas</option>
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="nivel" class="form-label fw-semibold small">Nivel Académico *</label>
							<select id="nivel" class="form-select" bind:value={nuevoPrograma.nivel} required>
								<option value="Pregrado">Pregrado</option>
								<option value="Especialización">Especialización</option>
								<option value="Maestría">Maestría</option>
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="creditos" class="form-label fw-semibold small">Créditos Totales *</label>
							<input
								id="creditos"
								type="number"
								class="form-control"
								min="60"
								max="200"
								required
								bind:value={nuevoPrograma.creditos}
							/>
						</div>
						<div class="col-12 col-md-3">
							<label for="estado" class="form-label fw-semibold small">Estado Inicial *</label>
							<select id="estado" class="form-select" bind:value={nuevoPrograma.estado} required>
								<option value="Activo">Activo</option>
								<option value="Inactivo">Inactivo</option>
							</select>
						</div>
						<div class="col-12 col-md-3 d-flex align-items-end">
							<button type="submit" class="btn btn-success w-100 shadow-sm fw-bold">
								<i class="bi bi-save2-fill me-1"></i>Guardar Programa
							</button>
						</div>
					</div>
				</form>
			</div>
		</section>
	{/if}

	<!-- Barra de Búsqueda y Filtros -->
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
							placeholder="Buscar por código o nombre de programa..."
							bind:value={busqueda}
						/>
					</div>
				</div>
				<div class="col-12 col-md-4">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroFac" class="text-nowrap small fw-semibold text-muted mb-0">Facultad:</label>
						<select id="filtroFac" class="form-select form-select-sm" bind:value={filtroFacultad}>
							<option value="todas">Todas las Facultades</option>
							<option value="Facultad de Ingeniería">Ingeniería</option>
							<option value="Facultad de Ciencias Económicas">Ciencias Económicas</option>
							<option value="Facultad de Artes y Diseño">Artes y Diseño</option>
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2 text-md-end">
					<span class="badge bg-light text-secondary border px-3 py-2">
						{programasFiltrados.length} Registros
					</span>
				</div>
			</div>
		</div>
	</section>

	<!-- Tabla de Listado de Programas -->
	<section class="card border-0 shadow-sm rounded-3">
		<div class="card-body p-0">
			<div class="table-responsive">
				<table class="table table-hover align-middle mb-0">
					<thead class="table-light text-uppercase small text-muted">
						<tr>
							<th class="ps-4">Código</th>
							<th>Nombre del Programa</th>
							<th>Facultad</th>
							<th>Nivel</th>
							<th>Créditos</th>
							<th>Estado</th>
							<th class="text-end pe-4">Acciones</th>
						</tr>
					</thead>
					<tbody>
						{#if programasFiltrados.length === 0}
							<tr>
								<td colspan="7" class="text-center py-4 text-muted">
									<i class="bi bi-inbox fs-3 d-block mb-1"></i>
									No se encontraron programas académicos con los criterios seleccionados.
								</td>
							</tr>
						{:else}
							{#each programasFiltrados as p}
								<tr>
									<td class="ps-4">
										<span class="badge bg-primary-subtle text-primary border border-primary-subtle font-monospace">
											{p.codigo}
										</span>
									</td>
									<td>
										<div class="fw-bold text-dark">{p.nombre}</div>
									</td>
									<td>
										<small class="text-secondary">{p.facultad}</small>
									</td>
									<td>
										<span class="badge bg-light text-dark border">{p.nivel}</span>
									</td>
									<td>
										<span class="fw-medium">{p.creditos}</span>
									</td>
									<td>
										<span class="badge {p.estado === 'Activo' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-danger-subtle text-danger'}">
											{p.estado}
										</span>
									</td>
									<td class="text-end pe-4">
										<button
											type="button"
											class="btn btn-sm btn-outline-danger"
											onclick={() => eliminarPrograma(p.id, p.nombre)}
											title="Eliminar Programa"
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
