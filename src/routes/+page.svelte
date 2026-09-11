<script>
	import StatCard from '$lib/components/StatCard.svelte';
	import {
		practicasStore,
		estudiantesStore,
		empresasStore,
		conveniosStore,
		evaluacionesStore,
		rolActivoStore
	} from '$lib/data/mockData.js';

	// Métricas calculadas
	let totalPracticas = $derived($practicasStore.length);
	let totalEstudiantes = $derived($estudiantesStore.length);
	let totalEmpresas = $derived($empresasStore.length);
	let totalConvenios = $derived($conveniosStore.length);
</script>

<svelte:head>
	<title>Inicio | Sistema de Gestión de Prácticas Profesionales</title>
</svelte:head>

<div class="container-fluid px-4 py-4">
	<!-- Banner Institucional de Bienvenida -->
	<section class="card border-0 bg-primary text-white shadow-sm rounded-4 mb-4 overflow-hidden">
		<div class="card-body p-4 p-lg-5">
			<div class="row align-items-center">
				<div class="col-lg-8">
					<span class="badge bg-warning text-dark px-3 py-2 rounded-pill fw-bold mb-3">
						<i class="bi bi-award-fill me-1"></i> Plataforma Académica Oficial
					</span>
					<h2 class="display-6 fw-bold mb-2">
						¡Bienvenido, {$rolActivoStore.usuario}!
					</h2>
					<p class="lead mb-4 text-white-50">
						Panel de control y monitoreo de prácticas profesionales. Estructura integral para vinculación de estudiantes, convenios empresariales, seguimiento de bitácoras y rúbricas de evaluación cuantitativa.
					</p>
					<div class="d-flex flex-wrap gap-2">
						<a href="/practicas" class="btn btn-warning text-dark fw-bold px-4 shadow-sm">
							<i class="bi bi-briefcase-fill me-2"></i>Ver Prácticas Activas
						</a>
						<a href="/estudiantes" class="btn btn-outline-light px-4">
							<i class="bi bi-people-fill me-2"></i>Directorio de Estudiantes
						</a>
						<a href="/seguridad" class="btn btn-outline-light px-3">
							<i class="bi bi-shield-lock me-1"></i>Matriz RBAC
						</a>
					</div>
				</div>
				<div class="col-lg-4 d-none d-lg-flex justify-content-center">
					<div class="bg-white bg-opacity-10 p-4 rounded-circle text-center" style="width: 180px; height: 180px; display: flex; align-items: center; justify-content: center;">
						<i class="bi bi-mortarboard fs-1 text-warning" style="font-size: 5rem !important;"></i>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Fila de Tarjetas Estadísticas (KPIs) -->
	<section class="row g-3 mb-4" aria-label="Métricas Principales">
		<StatCard
			title="Prácticas en Curso"
			value={totalPracticas.toString()}
			icon="bi-briefcase-fill"
			color="primary"
			description="Periodo 2026-I en ejecución"
			trend="+12% vs 2025-II"
		/>
		<StatCard
			title="Estudiantes Asignados"
			value={totalEstudiantes.toString()}
			icon="bi-people-fill"
			color="success"
			description="Con matrícula vigente"
			trend="100% Cobertura"
		/>
		<StatCard
			title="Empresas Aliadas"
			value={totalEmpresas.toString()}
			icon="bi-buildings-fill"
			color="info"
			description="Sectores TI, Banca, Salud"
			trend="Activas"
		/>
		<StatCard
			title="Convenios Vigentes"
			value={totalConvenios.toString()}
			icon="bi-file-earmark-check-fill"
			color="warning"
			description="Marco y Específicos"
			trend="Sin mora legal"
		/>
	</section>

	<div class="row g-4 mb-4">
		<!-- Tabla de Prácticas Recientes -->
		<div class="col-12 col-xl-8">
			<section class="card border-0 shadow-sm rounded-3 h-100">
				<header class="card-header bg-white py-3 border-0 d-flex align-items-center justify-content-between flex-wrap gap-2">
					<div>
						<h3 class="h5 fw-bold mb-0 text-dark">
							<i class="bi bi-clock-history text-primary me-2"></i>Monitoreo de Prácticas Recientes
						</h3>
						<small class="text-muted">Estado del avance de horas y asignación de tutores</small>
					</div>
					<a href="/practicas" class="btn btn-sm btn-outline-primary fw-medium">
						Ver Todo <i class="bi bi-arrow-right ms-1"></i>
					</a>
				</header>
				<div class="card-body p-0">
					<div class="table-responsive">
						<table class="table table-hover align-middle mb-0">
							<thead class="table-light text-uppercase small text-muted">
								<tr>
									<th class="ps-4">Estudiante</th>
									<th>Empresa</th>
									<th>Tutor Académico</th>
									<th style="min-width: 140px;">Progreso de Horas</th>
									<th>Estado</th>
									<th class="text-end pe-4">Acción</th>
								</tr>
							</thead>
							<tbody>
								{#each $practicasStore as p}
									{@const porcentaje = Math.round((p.horas_completadas / p.horas_totales) * 100)}
									<tr>
										<td class="ps-4">
											<div class="fw-bold text-dark">{p.estudiante_nombre}</div>
											<div class="small text-muted">{p.programa}</div>
										</td>
										<td>
											<div class="fw-medium">{p.empresa_nombre}</div>
											<div class="small text-muted">{p.modalidad}</div>
										</td>
										<td>
											<small class="text-secondary">{p.tutor_academico}</small>
										</td>
										<td>
											<div class="d-flex align-items-center justify-content-between small mb-1">
												<span>{p.horas_completadas} / {p.horas_totales} h</span>
												<span class="fw-bold">{porcentaje}%</span>
											</div>
											<div class="progress" style="height: 6px;" role="progressbar" aria-valuenow={porcentaje} aria-valuemin="0" aria-valuemax="100">
												<div
													class="progress-bar {porcentaje > 50 ? 'bg-success' : 'bg-primary'}"
													style="width: {porcentaje}%"
												></div>
											</div>
										</td>
										<td>
											{#if p.estado === 'En Proceso'}
												<span class="badge bg-success-subtle text-success border border-success-subtle">
													<i class="bi bi-check2-circle me-1"></i>En Proceso
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
											<a href="/practicas" class="btn btn-sm btn-light border" title="Detalles">
												<i class="bi bi-eye"></i>
											</a>
										</td>
									</tr>
								{/each}
							</tbody>
						</table>
					</div>
				</div>
			</section>
		</div>

		<!-- Panel Lateral: Acciones Rápidas y Guía de Usabilidad -->
		<div class="col-12 col-xl-4">
			<div class="d-flex flex-column gap-3">
				<!-- Tarjeta de Acciones Rápidas -->
				<section class="card border-0 shadow-sm rounded-3">
					<header class="card-header bg-white py-3 border-0">
						<h3 class="h6 fw-bold mb-0 text-dark">
							<i class="bi bi-lightning-charge-fill text-warning me-2"></i>Accesos Rápidos
						</h3>
					</header>
					<div class="card-body p-3 pt-0">
						<div class="list-group list-group-flush">
							<a href="/estudiantes" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between px-2 py-2 border-0 rounded-2">
								<div class="d-flex align-items-center gap-2">
									<i class="bi bi-person-plus-fill text-primary"></i>
									<span>Registrar Nuevo Estudiante</span>
								</div>
								<i class="bi bi-chevron-right text-muted small"></i>
							</a>
							<a href="/empresas" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between px-2 py-2 border-0 rounded-2">
								<div class="d-flex align-items-center gap-2">
									<i class="bi bi-building-add text-info"></i>
									<span>Inscribir Empresa Aliada</span>
								</div>
								<i class="bi bi-chevron-right text-muted small"></i>
							</a>
							<a href="/convenios" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between px-2 py-2 border-0 rounded-2">
								<div class="d-flex align-items-center gap-2">
									<i class="bi bi-file-earmark-plus text-success"></i>
									<span>Crear Convenio Marco</span>
								</div>
								<i class="bi bi-chevron-right text-muted small"></i>
							</a>
							<a href="/seguimientos" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between px-2 py-2 border-0 rounded-2">
								<div class="d-flex align-items-center gap-2">
									<i class="bi bi-journal-plus text-secondary"></i>
									<span>Registrar Bitácora Semanal</span>
								</div>
								<i class="bi bi-chevron-right text-muted small"></i>
							</a>
							<a href="/evaluaciones" class="list-group-item list-group-item-action d-flex align-items-center justify-content-between px-2 py-2 border-0 rounded-2">
								<div class="d-flex align-items-center gap-2">
									<i class="bi bi-star-fill text-warning"></i>
									<span>Diligenciar Rúbrica de Evaluación</span>
								</div>
								<i class="bi bi-chevron-right text-muted small"></i>
							</a>
						</div>
					</div>
				</section>

				<!-- Tarjeta de Información RBAC -->
				<section class="card border-0 shadow-sm rounded-3 bg-light border-start border-4 border-info">
					<div class="card-body p-3">
						<h4 class="h6 fw-bold text-dark d-flex align-items-center gap-2 mb-2">
							<i class="bi bi-shield-lock-fill text-info"></i> Control RBAC y Jerarquía
						</h4>
						<p class="small text-muted mb-2">
							El sistema aplica el principio de menor privilegio con 4 rangos de autoridad:
						</p>
						<ul class="list-unstyled small mb-0 d-flex flex-column gap-1">
							<li class="d-flex align-items-center justify-content-between bg-white p-2 rounded border">
								<span class="fw-bold">Nivel 1: Administrador</span>
								<span class="badge bg-danger">Total</span>
							</li>
							<li class="d-flex align-items-center justify-content-between bg-white p-2 rounded border">
								<span class="fw-bold">Nivel 2: Coordinador</span>
								<span class="badge bg-primary">Gestión</span>
							</li>
							<li class="d-flex align-items-center justify-content-between bg-white p-2 rounded border">
								<span class="fw-bold">Nivel 3: Profesor</span>
								<span class="badge bg-success">Supervisión</span>
							</li>
							<li class="d-flex align-items-center justify-content-between bg-white p-2 rounded border">
								<span class="fw-bold">Nivel 4: Estudiante</span>
								<span class="badge bg-secondary">Consulta</span>
							</li>
						</ul>
					</div>
				</section>
			</div>
		</div>
	</div>
</div>
