<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import { empresasStore } from '$lib/data/mockData.js';

	let busqueda = $state('');
	let filtroSector = $state('todos');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	let nuevaEmpresa = $state({
		nit: '',
		razon_social: '',
		sector: 'Tecnología y Software',
		contacto: '',
		correo: '',
		telefono: '',
		ciudad: 'Bogotá D.C.',
		estado: 'Activo'
	});

	let empresasFiltradas = $derived(
		$empresasStore.filter((e) => {
			const matchTexto =
				e.razon_social.toLowerCase().includes(busqueda.toLowerCase()) ||
				e.nit.includes(busqueda) ||
				e.contacto.toLowerCase().includes(busqueda.toLowerCase());
			const matchSector = filtroSector === 'todos' || e.sector === filtroSector;
			return matchTexto && matchSector;
		})
	);

	function registrarEmpresa(event) {
		event.preventDefault();
		const id = $empresasStore.length ? Math.max(...$empresasStore.map((e) => e.id)) + 1 : 1;
		empresasStore.update((lista) => [
			{ id, ...nuevaEmpresa },
			...lista
		]);
		mensajeAlerta = `¡Empresa "${nuevaEmpresa.razon_social}" registrada satisfactoriamente!`;
		nuevaEmpresa = {
			nit: '',
			razon_social: '',
			sector: 'Tecnología y Software',
			contacto: '',
			correo: '',
			telefono: '',
			ciudad: 'Bogotá D.C.',
			estado: 'Activo'
		};
		mostrarFormulario = false;
	}

	function eliminarEmpresa(id, nombre) {
		if (confirm(`¿Desea dar de baja a la empresa "${nombre}"?`)) {
			empresasStore.update((lista) => lista.filter((e) => e.id !== id));
			mensajeAlerta = `Empresa "${nombre}" eliminada correctamente.`;
		}
	}
</script>

<svelte:head>
	<title>Empresas Aliadas | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Empresas Aliadas', href: '/empresas' }]} />

	<!-- Encabezado -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<h2 class="h3 fw-bold text-dark mb-1">
				<i class="bi bi-buildings-fill text-info me-2"></i>Directorio de Empresas Aliadas
			</h2>
			<p class="text-muted mb-0 small">
				Gestión de organizaciones vinculadas mediante convenios para prácticas empresariales y profesionales.
			</p>
		</div>
		<button
			type="button"
			class="btn btn-info text-dark fw-bold d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-building-add'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : 'Inscribir Empresa'}</span>
		</button>
	</header>

	{#if mensajeAlerta}
		<div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
			<i class="bi bi-check-circle-fill me-2"></i>{mensajeAlerta}
			<button type="button" class="btn-close" onclick={() => (mensajeAlerta = '')} aria-label="Cerrar"></button>
		</div>
	{/if}

	<!-- Formulario de Inscripción -->
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-info">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-dark">
					<i class="bi bi-plus-circle-fill text-info me-2"></i>Inscribir Nueva Empresa Aliada
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={registrarEmpresa}>
					<div class="row g-3">
						<div class="col-12 col-md-3">
							<label for="nit" class="form-label fw-semibold small">NIT Empresa *</label>
							<input id="nit" type="text" class="form-control" placeholder="900.123.456-1" required bind:value={nuevaEmpresa.nit} />
						</div>
						<div class="col-12 col-md-5">
							<label for="razon_social" class="form-label fw-semibold small">Razón Social *</label>
							<input id="razon_social" type="text" class="form-control" placeholder="Nombre legal de la compañía" required bind:value={nuevaEmpresa.razon_social} />
						</div>
						<div class="col-12 col-md-4">
							<label for="sector" class="form-label fw-semibold small">Sector Económico *</label>
							<select id="sector" class="form-select" bind:value={nuevaEmpresa.sector} required>
								<option value="Tecnología y Software">Tecnología y Software</option>
								<option value="Financiero y Banca">Financiero y Banca</option>
								<option value="Farmacéutico y Salud">Farmacéutico y Salud</option>
								<option value="Transporte y Cadena de Suministro">Transporte y Cadena de Suministro</option>
								<option value="Construcción e Infraestructura">Construcción e Infraestructura</option>
								<option value="Comercio y Retail">Comercio y Retail</option>
							</select>
						</div>
						<div class="col-12 col-md-4">
							<label for="contacto" class="form-label fw-semibold small">Contacto / Representante *</label>
							<input id="contacto" type="text" class="form-control" placeholder="Nombre completo del enlace" required bind:value={nuevaEmpresa.contacto} />
						</div>
						<div class="col-12 col-md-4">
							<label for="correo" class="form-label fw-semibold small">Correo Electrónico *</label>
							<input id="correo" type="email" class="form-control" placeholder="contacto@empresa.com" required bind:value={nuevaEmpresa.correo} />
						</div>
						<div class="col-12 col-md-4">
							<label for="telefono" class="form-label fw-semibold small">Teléfono / PBX *</label>
							<input id="telefono" type="tel" class="form-control" placeholder="601-555-0100" required bind:value={nuevaEmpresa.telefono} />
						</div>
						<div class="col-12 col-md-4">
							<label for="ciudad" class="form-label fw-semibold small">Ciudad Sede *</label>
							<input id="ciudad" type="text" class="form-control" placeholder="Bogotá, Medellín, etc." required bind:value={nuevaEmpresa.ciudad} />
						</div>
						<div class="col-12 col-md-4">
							<label for="estadoEmp" class="form-label fw-semibold small">Estado del Registro *</label>
							<select id="estadoEmp" class="form-select" bind:value={nuevaEmpresa.estado} required>
								<option value="Activo">Activo</option>
								<option value="Inactivo">Inactivo</option>
							</select>
						</div>
						<div class="col-12 col-md-4 d-flex align-items-end">
							<button type="submit" class="btn btn-success w-100 fw-bold shadow-sm">
								<i class="bi bi-building-check me-1"></i>Guardar Empresa
							</button>
						</div>
					</div>
				</form>
			</div>
		</section>
	{/if}

	<!-- Barra de Filtros -->
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
							placeholder="Buscar por NIT, Razón Social o Contacto..."
							bind:value={busqueda}
						/>
					</div>
				</div>
				<div class="col-12 col-md-4">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroSec" class="text-nowrap small fw-semibold text-muted mb-0">Sector:</label>
						<select id="filtroSec" class="form-select form-select-sm" bind:value={filtroSector}>
							<option value="todos">Todos los Sectores</option>
							<option value="Tecnología y Software">Tecnología y Software</option>
							<option value="Financiero y Banca">Financiero y Banca</option>
							<option value="Farmacéutico y Salud">Farmacéutico y Salud</option>
							<option value="Transporte y Cadena de Suministro">Transporte</option>
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2 text-md-end">
					<span class="badge bg-light text-secondary border px-3 py-2">
						{empresasFiltradas.length} Empresas
					</span>
				</div>
			</div>
		</div>
	</section>

	<!-- Tabla de Empresas -->
	<section class="card border-0 shadow-sm rounded-3">
		<div class="card-body p-0">
			<div class="table-responsive">
				<table class="table table-hover align-middle mb-0">
					<thead class="table-light text-uppercase small text-muted">
						<tr>
							<th class="ps-4">NIT</th>
							<th>Razón Social</th>
							<th>Sector Económico</th>
							<th>Contacto Principal</th>
							<th>Ciudad</th>
							<th>Estado</th>
							<th class="text-end pe-4">Acciones</th>
						</tr>
					</thead>
					<tbody>
						{#if empresasFiltradas.length === 0}
							<tr>
								<td colspan="7" class="text-center py-4 text-muted">
									<i class="bi bi-buildings fs-3 d-block mb-1"></i>
									No se encontraron empresas con los filtros aplicados.
								</td>
							</tr>
						{:else}
							{#each empresasFiltradas as e}
								<tr>
									<td class="ps-4">
										<span class="font-monospace text-muted small">{e.nit}</span>
									</td>
									<td>
										<div class="fw-bold text-dark">{e.razon_social}</div>
										<small class="text-muted"><i class="bi bi-envelope me-1"></i>{e.correo}</small>
									</td>
									<td>
										<span class="badge bg-info-subtle text-info border border-info-subtle">
											{e.sector}
										</span>
									</td>
									<td>
										<div>{e.contacto}</div>
										<small class="text-muted"><i class="bi bi-telephone me-1"></i>{e.telefono}</small>
									</td>
									<td>
										<span class="text-secondary small">{e.ciudad}</span>
									</td>
									<td>
										<span class="badge {e.estado === 'Activo' ? 'bg-success-subtle text-success border border-success-subtle' : 'bg-danger-subtle text-danger'}">
											{e.estado}
										</span>
									</td>
									<td class="text-end pe-4">
										<button
											type="button"
											class="btn btn-sm btn-outline-danger"
											onclick={() => eliminarEmpresa(e.id, e.razon_social)}
											title="Eliminar Empresa"
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
