<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import { seguimientosStore, practicasStore } from '$lib/data/mockData.js';

	let busqueda = $state('');
	let filtroEstado = $state('todos');
	let mostrarFormulario = $state(false);
	let mensajeAlerta = $state('');

	let nuevoSeguimiento = $state({
		practica_id: 1,
		numero_semana: 1,
		fecha_registro: '2026-04-10',
		horas_reportadas: 40,
		actividad: '',
		observaciones: '',
		estado: 'En Revisión'
	});

	let seguimientosFiltrados = $derived(
		$seguimientosStore.filter((s) => {
			const matchTexto =
				s.estudiante_nombre.toLowerCase().includes(busqueda.toLowerCase()) ||
				s.actividad.toLowerCase().includes(busqueda.toLowerCase()) ||
				s.observaciones.toLowerCase().includes(busqueda.toLowerCase());
			const matchEstado = filtroEstado === 'todos' || s.estado === filtroEstado;
			return matchTexto && matchEstado;
		})
	);

	function registrarSeguimiento(event) {
		event.preventDefault();
		const prac = $practicasStore.find((p) => p.id === Number(nuevoSeguimiento.practica_id));
		const nombreEstudiante = prac ? prac.estudiante_nombre : 'Estudiante';

		const id = $seguimientosStore.length ? Math.max(...$seguimientosStore.map((s) => s.id)) + 1 : 1;
		seguimientosStore.update((lista) => [
			{
				id,
				...nuevoSeguimiento,
				estudiante_nombre: nombreEstudiante
			},
			...lista
		]);

		mensajeAlerta = `¡Bitácora de la semana #${nuevoSeguimiento.numero_semana} registrada con éxito para ${nombreEstudiante}!`;
		nuevoSeguimiento = {
			practica_id: 1,
			numero_semana: 1,
			fecha_registro: '2026-04-10',
			horas_reportadas: 40,
			actividad: '',
			observaciones: '',
			estado: 'En Revisión'
		};
		mostrarFormulario = false;
	}

	function cambiarEstado(id, nuevoEstado) {
		seguimientosStore.update((l) =>
			l.map((s) => (s.id === id ? { ...s, estado: nuevoEstado } : s))
		);
		mensajeAlerta = `Bitácora actualizada a estado: "${nuevoEstado}".`;
	}

	function eliminarSeguimiento(id) {
		if (confirm('¿Desea eliminar este registro de bitácora?')) {
			seguimientosStore.update((l) => l.filter((s) => s.id !== id));
			mensajeAlerta = 'Registro de bitácora eliminado.';
		}
	}
</script>

<svelte:head>
	<title>Seguimientos y Bitácoras | SGPP</title>
</svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Seguimientos y Bitácoras', href: '/seguimientos' }]} />

	<!-- Encabezado -->
	<header class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-3 mb-4">
		<div>
			<h2 class="h3 fw-bold text-dark mb-1">
				<i class="bi bi-journal-check text-secondary me-2"></i>Seguimiento Periódico de Prácticas
			</h2>
			<p class="text-muted mb-0 small">
				Bitácoras semanales de avance de actividades, cómputo de horas laboradas y retroalimentación de tutores.
			</p>
		</div>
		<button
			type="button"
			class="btn btn-secondary text-white fw-bold d-flex align-items-center gap-2 shadow-sm"
			onclick={() => (mostrarFormulario = !mostrarFormulario)}
		>
			<i class="bi {mostrarFormulario ? 'bi-x-lg' : 'bi-journal-plus'}"></i>
			<span>{mostrarFormulario ? 'Cerrar Formulario' : 'Registrar Bitácora'}</span>
		</button>
	</header>

	{#if mensajeAlerta}
		<div class="alert alert-success alert-dismissible fade show shadow-sm" role="alert">
			<i class="bi bi-check-circle-fill me-2"></i>{mensajeAlerta}
			<button type="button" class="btn-close" onclick={() => (mensajeAlerta = '')} aria-label="Cerrar"></button>
		</div>
	{/if}

	<!-- Formulario de Bitácora -->
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm rounded-3 mb-4 border-start border-4 border-secondary">
			<header class="card-header bg-white py-3">
				<h3 class="h5 fw-bold mb-0 text-dark">
					<i class="bi bi-pencil-fill text-secondary me-2"></i>Reporte Semanal de Actividades (Bitácora)
				</h3>
			</header>
			<div class="card-body p-4">
				<form onsubmit={registrarSeguimiento}>
					<div class="row g-3">
						<div class="col-12 col-md-6">
							<label for="pracSeg" class="form-label fw-semibold small">Práctica del Estudiante *</label>
							<select id="pracSeg" class="form-select" bind:value={nuevoSeguimiento.practica_id} required>
								{#each $practicasStore as p}
									<option value={p.id}>{p.estudiante_nombre} - {p.empresa_nombre} ({p.cargo_estudiante})</option>
								{/each}
							</select>
						</div>
						<div class="col-12 col-md-2">
							<label for="semSeg" class="form-label fw-semibold small">No. Semana *</label>
							<input id="semSeg" type="number" min="1" max="20" class="form-control" required bind:value={nuevoSeguimiento.numero_semana} />
						</div>
						<div class="col-12 col-md-2">
							<label for="fRegSeg" class="form-label fw-semibold small">Fecha Reporte *</label>
							<input id="fRegSeg" type="date" class="form-control" required bind:value={nuevoSeguimiento.fecha_registro} />
						</div>
						<div class="col-12 col-md-2">
							<label for="horSeg" class="form-label fw-semibold small">Horas Reportadas *</label>
							<input id="horSeg" type="number" min="1" max="50" class="form-control" required bind:value={nuevoSeguimiento.horas_reportadas} />
						</div>
						<div class="col-12 col-md-8">
							<label for="actSeg" class="form-label fw-semibold small">Descripción Detallada de Tareas Ejecutadas *</label>
							<textarea id="actSeg" class="form-control" rows="3" placeholder="Detalle los avances técnicos, entregables y metodologías aplicadas durante la semana..." required bind:value={nuevoSeguimiento.actividad}></textarea>
						</div>
						<div class="col-12 col-md-4">
							<label for="obsSeg" class="form-label fw-semibold small">Observaciones del Tutor</label>
							<textarea id="obsSeg" class="form-control" rows="3" placeholder="Comentarios del asesor o dificultades encontradas..." bind:value={nuevoSeguimiento.observaciones}></textarea>
						</div>
						<div class="col-12 d-flex justify-content-end">
							<button type="submit" class="btn btn-success fw-bold px-4 shadow-sm">
								<i class="bi bi-cloud-upload-fill me-1"></i>Guardar Bitácora
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
							placeholder="Buscar por estudiante, actividad u observaciones..."
							bind:value={busqueda}
						/>
					</div>
				</div>
				<div class="col-12 col-md-4">
					<div class="d-flex align-items-center gap-2">
						<label for="filtroEstSeg" class="text-nowrap small fw-semibold text-muted mb-0">Estado:</label>
						<select id="filtroEstSeg" class="form-select form-select-sm" bind:value={filtroEstado}>
							<option value="todos">Todos los Estados</option>
							<option value="Aprobado">Aprobado</option>
							<option value="En Revisión">En Revisión</option>
							<option value="Observado">Observado</option>
						</select>
					</div>
				</div>
				<div class="col-12 col-md-2 text-md-end">
					<span class="badge bg-light text-secondary border px-3 py-2">
						{seguimientosFiltrados.length} Bitácoras
					</span>
				</div>
			</div>
		</div>
	</section>

	<!-- Tabla de Seguimientos -->
	<section class="card border-0 shadow-sm rounded-3">
		<div class="card-body p-0">
			<div class="table-responsive">
				<table class="table table-hover align-middle mb-0">
					<thead class="table-light text-uppercase small text-muted">
						<tr>
							<th class="ps-4">Semana</th>
							<th>Estudiante</th>
							<th>Fecha y Horas</th>
							<th style="min-width: 250px;">Actividades Ejecutadas</th>
							<th>Observaciones del Asesor</th>
							<th>Estado</th>
							<th class="text-end pe-4">Acciones</th>
						</tr>
					</thead>
					<tbody>
						{#if seguimientosFiltrados.length === 0}
							<tr>
								<td colspan="7" class="text-center py-4 text-muted">No se encontraron registros de bitácoras.</td>
							</tr>
						{:else}
							{#each seguimientosFiltrados as s}
								<tr>
									<td class="ps-4">
										<span class="badge bg-primary text-white font-monospace">Semana {s.numero_semana}</span>
									</td>
									<td>
										<div class="fw-bold text-dark">{s.estudiante_nombre}</div>
									</td>
									<td>
										<div class="small fw-medium"><i class="bi bi-clock me-1 text-primary"></i>{s.horas_reportadas} Horas</div>
										<small class="text-muted"><i class="bi bi-calendar3 me-1"></i>{s.fecha_registro}</small>
									</td>
									<td>
										<div class="small text-secondary">{s.actividad}</div>
									</td>
									<td>
										<small class="text-muted fst-italic">{s.observaciones || 'Sin observaciones registradas'}</small>
									</td>
									<td>
										{#if s.estado === 'Aprobado'}
											<span class="badge bg-success-subtle text-success border border-success-subtle">
												<i class="bi bi-check-circle me-1"></i>Aprobado
											</span>
										{:else}
											<span class="badge bg-warning-subtle text-warning border border-warning-subtle">
												<i class="bi bi-hourglass-split me-1"></i>{s.estado}
											</span>
										{/if}
									</td>
									<td class="text-end pe-4">
										<div class="btn-group btn-group-sm">
											{#if s.estado !== 'Aprobado'}
												<button
													type="button"
													class="btn btn-outline-success"
													onclick={() => cambiarEstado(s.id, 'Aprobado')}
													title="Aprobar Bitácora"
												>
													<i class="bi bi-check-lg"></i>
												</button>
											{/if}
											<button
												type="button"
												class="btn btn-outline-danger"
												onclick={() => eliminarSeguimiento(s.id)}
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
