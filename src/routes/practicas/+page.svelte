<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import {
		practicasStore,
		estudiantesStore,
		empresasStore,
		conveniosStore,
		tutoresAcademicosStore,
		tutoresEmpresarialesStore
	} from '$lib/data/mockData.js';

	let busqueda = $state('');
	let filtroEstado = $state('todos');
	let filtroModalidad = $state('todas');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	let nuevaPractica = $state({
		estudiante_id: 1,
		empresa_id: 1,
		convenio_id: 1,
		tutor_academico_id: 1,
		tutor_empresarial_id: 1,
		cargo_estudiante: '',
		fecha_inicio: '2026-03-01',
		fecha_fin: '2026-08-31',
		horas_totales: 640,
		horas_completadas: 0,
		modalidad: 'Híbrida',
		estado: 'Pendiente Aprobación'
	});

	let practicasFiltradas = $derived(
		$practicasStore.filter((p) => {
			const matchTexto =
				p.estudiante_nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
				p.empresa_nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
				p.cargo_estudiante.toLowerCase().includes(busqueda.toLowerCase()) ||
				p.programa.toLowerCase().includes(busqueda.toLowerCase());
			const matchEstado = filtroEstado === 'todos' || p.estado === filtroEstado;
			const matchModalidad = filtroModalidad === 'todas' || p.modalidad === filtroModalidad;
			return matchTexto && matchEstado && matchModalidad;
		})
	);

	function registrarPractica(event) {
		event.preventDefault();
		const est = $estudiantesStore.find((e) => e.id === Number(nuevaPractica.estudiante_id));
		const emp = $empresasStore.find((e) => e.id === Number(nuevaPractica.empresa_id));
		const conv = $conveniosStore.find((c) => c.id === Number(nuevaPractica.convenio_id));
		const tutAc = $tutoresAcademicosStore.find((t) => t.id === Number(nuevaPractica.tutor_academico_id));
		const tutEmp = $tutoresEmpresarialesStore.find((t) => t.id === Number(nuevaPractica.tutor_empresarial_id));

		const id = $practicasStore.length ? Math.max(...$practicasStore.map((p) => p.id)) + 1 : 1;

		practicasStore.update((lista) => [
			{
				id,
				estudiante_id: nuevaPractica.estudiante_id,
				estudiante_nombre: est ? `${est.nombres} ${est.apellidos}` : 'Estudiante Asignado',
				programa: est ? est.programa : 'Ingeniería de Sistemas',
				empresa_id: nuevaPractica.empresa_id,
				empresa_nombre: emp ? emp.razon_social : 'Empresa Aliada',
				convenio_codigo: conv ? conv.codigo : 'CONV-2026-001',
				tutor_academico: tutAc ? `${tutAc.nombres} ${tutAc.apellidos}` : 'Tutor Académico',
				tutor_empresarial: tutEmp ? `${tutEmp.nombres} ${tutEmp.apellidos}` : 'Tutor Empresarial',
				cargo_estudiante: nuevaPractica.cargo_estudiante || 'Practicante Profesional',
				fecha_inicio: nuevaPractica.fecha_inicio,
				fecha_fin: nuevaPractica.fecha_fin,
				horas_totales: nuevaPractica.horas_totales,
				horas_completadas: nuevaPractica.horas_completadas,
				modalidad: nuevaPractica.modalidad,
				estado: nuevaPractica.estado
			},
			...lista
		]);

		mensajeAlerta = `¡Práctica profesional asignada exitosamente para ${est ? est.nombres : 'el estudiante'}!`;
		nuevaPractica = {
			estudiante_id: 1,
			empresa_id: 1,
			convenio_id: 1,
			tutor_academico_id: 1,
			tutor_empresarial_id: 1,
			cargo_estudiante: '',
			fecha_inicio: '2026-03-01',
			fecha_fin: '2026-08-31',
			horas_totales: 640,
			horas_completadas: 0,
			modalidad: 'Híbrida',
			estado: 'Pendiente Aprobación'
		};
		mostrarFormulario = false;
	}

	function cambiarEstadoPractica(id, nuevoEstado) {
		practicasStore.update((lista) =>
			lista.map((p) => (p.id === id ? { ...p, estado: nuevoEstado } : p))
		);
		mensajeAlerta = `Estado de la práctica actualizado a: "${nuevoEstado}".`;
	}

	function eliminarPractica(id, nombre) {
		if (confirm(`¿Está seguro de eliminar la práctica de "${nombre}"?`)) {
			practicasStore.update((l) => l.filter((p) => p.id !== id));
			mensajeAlerta = `Práctica eliminada correctamente.`;
		}
	}
</script>

<svelte:head>
	<title>Prácticas Profesionales | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Prácticas Profesionales', href: '/practicas' }]} />

	<!-- Encabezado -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<div class="d-flex align-items-center gap-2">
				<h2 class="h3 fw-bold text-dark mb-1">
					<i class="bi bi-briefcase-fill text-primary me-2"></i>Gestión Integral de Prácticas Profesionales
				</h2>
				<span class="badge bg-danger">Módulo Central</span>
			</div>
			<p class="text-muted mb-0 small">
				Vinculación oficial entre Estudiantes, Empresas Aliadas, Convenios y Tutores asignados.
			</p>
		</div>
		<button
			type="button"
			class="btn btn-primary fw-bold d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-plus-circle-fill'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : 'Asignar Nueva Práctica'}</span>
		</button>
	</header>

	{#if mensajeAlerta}
		<div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
			<i class="bi bi-check-circle-fill me-2"></i>{mensajeAlerta}
			<button type="button" class="btn-close" onclick={() => (mensajeAlerta = '')} aria-label="Cerrar"></button>
		</div>
	{/if}

	<!-- Formulario de Asignación -->
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-primary">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-primary">
					<i class="bi bi-file-earmark-person-fill me-2"></i>Acta de Inicio / Asignación de Práctica
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={registrarPractica}>
					<div class="row g-3">
						<div class="col-12 col-md-6">
							<label for="estPract" class="form-label fw-semibold small">Estudiante Postulante *</label>
							<select id="estPract" class="form-select" bind:value={nuevaPractica.estudiante_id} required>
								{#each $estudiantesStore as e}
									<option value={e.id}>{e.nombres} {e.apellidos} - {e.programa} ({e.documento})</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-6">
							<label for="empPract" class="form-label fw-semibold small">Empresa de Destino *</label>
							<select id="empPract" class="form-select" bind:value={nuevaPractica.empresa_id} required>
								{#each $empresasStore as emp}
									<option value={emp.id}>{emp.razon_social} ({emp.ciudad})</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-4">
							<label for="convPract" class="form-label fw-semibold small">Convenio que Ampara *</label>
							<select id="convPract" class="form-select" bind:value={nuevaPractica.convenio_id} required>
								{#each $conveniosStore as conv}
									<option value={conv.id}>{conv.codigo} - {conv.tipo}</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-4">
							<label for="tutAcPract" class="form-label fw-semibold small">Tutor Académico (Docente) *</label>
							<select id="tutAcPract" class="form-select" bind:value={nuevaPractica.tutor_academico_id} required>
								{#each $tutoresAcademicosStore as tut}
									<option value={tut.id}>{tut.nombres} {tut.apellidos} ({tut.departamento})</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-4">
							<label for="tutEmpPract" class="form-label fw-semibold small">Tutor Empresarial (Mentor) *</label>
							<select id="tutEmpPract" class="form-select" bind:value={nuevaPractica.tutor_empresarial_id} required>
								{#each $tutoresEmpresarialesStore as tut}
									<option value={tut.id}>{tut.nombres} {tut.apellidos} - {tut.empresa}</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-4">
							<label for="cargoPract" class="form-label fw-semibold small">Cargo / Función Asignada *</label>
							<input id="cargoPract" type="text" class="form-control" placeholder="Ej: Desarrollador Backend Junior" required bind:value={nuevaPractica.cargo_estudiante} />
						</div>
						<div class="col-12 col-md-2">
							<label for="modPract" class="form-label fw-semibold small">Modalidad *</label>
							<select id="modPract" class="form-select" bind:value={nuevaPractica.modalidad} required>
								<option value="Híbrida">Híbrida</option>
								<option value="Presencial">Presencial</option>
								<option value="Remota">Remota</option>
							</select>
						</div>
						<div class="col-12 col-md-3">
							<label for="fIniPract" class="form-label fw-semibold small">Fecha Inicio *</label>
							<input id="fIniPract" type="date" class="form-control" required bind:value={nuevaPractica.fecha_inicio} />
						</div>
						<div class="col-12 col-md-3">
							<label for="fFinPract" class="form-label fw-semibold small">Fecha Fin *</label>
							<input id="fFinPract" type="date" class="form-control" required bind:value={nuevaPractica.fecha_fin} />
						</div>
						<div class="col-12 col-md-3">
							<label for="horTotPract" class="form-label fw-semibold small">Horas Totales Reglamentarias *</label>
							<input id="horTotPract" type="number" class="form-control" min="320" max="960" required bind:value={nuevaPractica.horas_totales} />
						</div>
						<div class="col-12 col-md-3">
							<label for="estadoPract" class="form-label fw-semibold small">Estado Inicial *</label>
							<select id="estadoPract" class="form-select" bind:value={nuevaPractica.estado} required>
								<option value="En Proceso">En Proceso</option>
								<option value="Pendiente Aprobación">Pendiente Aprobación</option>
								<option value="Finalizada">Finalizada</option>
							</select>
						</div>
						<div class="col-12 col-md-6 d-flex align-items-end justify-content-end">
							<button type="submit" class="btn btn-success fw-bold px-4 shadow-sm">
								<i class="bi bi-check-all me-1"></i>Formalizar Vinculación
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
				<div class="col-12 col-md-5">
					<div class="input-group">
						<span class="input-group-text bg-light border-end-0">
							<i class="bi bi-search text-muted"></i>
						</span>
						<input
							type="search"
							class="form-control border-start-0"
							placeholder="Buscar por estudiante, empresa, cargo o carrera..."
							bind:value={busqueda}
						/>
					</div>
				</div>
				<div class="col-12 col-md-3">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroEst" class="text-nowrap small fw-semibold text-muted mb-0">Estado:</label>
						<select id="filtroEst" class="form-select form-select-sm" bind:value={filtroEstado}>
							<option value="todos">Todos los Estados</option>
							<option value="En Proceso">En Proceso</option>
							<option value="Pendiente Aprobación">Pendiente</option>
							<option value="Finalizada">Finalizada</option>
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroMod" class="text-nowrap small fw-semibold text-muted mb-0">Modalidad:</label>
						<select id="filtroMod" class="form-select form-select-sm" bind:value={filtroModalidad}>
							<option value="todas">Todas</option>
							<option value="Híbrida">Híbrida</option>
							<option value="Presencial">Presencial</option>
							<option value="Remota">Remota</option>
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2 text-md-end">
					<span class="badge bg-light text-secondary border px-3 py-2">
						{practicasFiltradas.length} Prácticas
					</span>
				</div>
			</div>
		</div>
	</section>

	<!-- Tabla Maestra de Prácticas -->
	<section class="card border-0 shadow-sm rounded-3">
		<div class="card-body p-0">
			<div class="table-responsive">
				<table class="table table-hover align-middle mb-0">
					<thead class="table-light text-uppercase small text-muted">
						<tr>
							<th class="ps-4">Estudiante y Carrera</th>
							<th>Empresa y Cargo</th>
							<th>Convenio</th>
							<th>Tutores Asignados</th>
							<th style="min-width: 140px;">Progreso de Horas</th>
							<th>Estado</th>
							<th class="text-end pe-4">Acciones</th>
						</tr>
					</thead>
					<tbody>
						{#if practicasFiltradas.length === 0}
							<tr>
								<td colspan="7" class="text-center py-4 text-muted">No se encontraron prácticas con los criterios indicados.</td>
							</tr>
						{:else}
							{#each practicasFiltradas as p}
								{@const pct = Math.round((p.horas_completadas / p.horas_totales) * 100)}
								<tr>
									<td class="ps-4">
										<div class="fw-bold text-dark">{p.estudiante_nombre}</div>
										<small class="text-muted">{p.programa}</small>
									</td>
									<td>
										<div class="fw-medium text-dark">{p.empresa_nombre}</div>
										<small class="badge bg-light text-dark border">{p.cargo_estudiante}</small>
										<span class="badge bg-secondary-subtle text-secondary ms-1">{p.modalidad}</span>
									</td>
									<td>
										<span class="badge bg-warning-subtle text-dark border font-monospace">{p.convenio_codigo}</span>
									</td>
									<td>
										<div class="small">
											<i class="bi bi-mortarboard me-1 text-primary"></i>{p.tutor_academico}
										</div>
										<div class="small text-muted">
											<i class="bi bi-building me-1 text-info"></i>{p.tutor_empresarial}
										</div>
									</td>
									<td>
										<div class="d-flex align-items-center justify-content-between small mb-1">
											<span>{p.horas_completadas} / {p.horas_totales} h</span>
											<span class="fw-bold">{pct}%</span>
										</div>
										<div class="progress" style="height: 6px;">
											<div class="progress-bar {pct > 50 ? 'bg-success' : 'bg-primary'}" style="width: {pct}%"></div>
										</div>
										<small class="text-muted d-block mt-1" style="font-size: 0.7rem;">
											{p.fecha_inicio} al {p.fecha_fin}
										</small>
									</td>
									<td>
										{#if p.estado === 'En Proceso'}
											<span class="badge bg-success-subtle text-success border border-success-subtle">
												<i class="bi bi-play-circle me-1"></i>En Proceso
											</span>
										{:else if p.estado === 'Pendiente Aprobación'}
											<span class="badge bg-warning-subtle text-warning border border-warning-subtle">
												<i class="bi bi-hourglass-split me-1"></i>Pendiente
											</span>
										{:else}
											<span class="badge bg-secondary">{p.estado}</span>
										{/if}
									</td>
									<td class="text-end pe-4">
										<div class="btn-group btn-group-sm">
											{#if p.estado === 'Pendiente Aprobación'}
												<button
													type="button"
													class="btn btn-outline-success"
													onclick={() => cambiarEstadoPractica(p.id, 'En Proceso')}
													title="Aprobar Práctica"
												>
													<i class="bi bi-check-lg"></i>
												</button>
											{/if}
											<button
												type="button"
												class="btn btn-outline-danger"
												onclick={() => eliminarPractica(p.id, p.estudiante_nombre)}
												title="Eliminar Registro"
											>
												<i class="bi bi-trash"></i>
											</button>
										</div>
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
