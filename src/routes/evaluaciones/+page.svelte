<script>
	import Breadcrumb from '$lib/components/Breadcrumb.svelte';
	import { evaluacionesStore, practicasStore } from '$lib/data/mockData.js';

	let mostrarFormulario = $state(false);
	let busqueda = $state('');
	let mensaje = $state('');
	let nueva = $state({ practica_id: 1, tipo: 'Evaluación de Medio Término', competencia_tecnica: 4, competencia_actitudinal: 4, puntualidad: 4, observaciones: '' });
	let evaluacionesFiltradas = $derived($evaluacionesStore.filter((e) =>
		e.estudiante_nombre.toLowerCase().includes(busqueda.toLowerCase()) || e.tipo.toLowerCase().includes(busqueda.toLowerCase())
	));

	function guardar(event) {
		event.preventDefault();
		const practica = $practicasStore.find((p) => p.id === Number(nueva.practica_id));
		const promedio = ((Number(nueva.competencia_tecnica) + Number(nueva.competencia_actitudinal) + Number(nueva.puntualidad)) / 3).toFixed(1);
		evaluacionesStore.update((lista) => [{
			id: lista.length + 1, practica_id: Number(nueva.practica_id), estudiante_nombre: practica?.estudiante_nombre ?? 'Estudiante',
			tipo: nueva.tipo, competencia_tecnica: Number(nueva.competencia_tecnica), competencia_actitudinal: Number(nueva.competencia_actitudinal),
			puntualidad: Number(nueva.puntualidad), calificacion_final: Number(promedio), observaciones: nueva.observaciones,
			evaluador: 'Coordinación de Prácticas', fecha: '2026-09-11', estado: 'Aprobada'
		}, ...lista]);
		mensaje = 'La evaluación fue registrada correctamente.';
		mostrarFormulario = false;
	}
</script>

<svelte:head><title>Evaluaciones | SGPP</title></svelte:head>

<div class="container-fluid px-4 py-3">
	<Breadcrumb items={[{ label: 'Evaluaciones', href: '/evaluaciones' }]} />
	<header class="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 mb-4">
		<div><h2 class="h3 fw-bold mb-1"><i class="bi bi-star-half text-warning me-2"></i>Evaluación de Prácticas</h2><p class="text-muted mb-0">Rúbricas cuantitativas para valorar el desempeño profesional.</p></div>
		<button class="btn btn-primary shadow-sm" type="button" onclick={() => mostrarFormulario = !mostrarFormulario}><i class="bi bi-plus-circle me-2"></i>{mostrarFormulario ? 'Cerrar formulario' : 'Nueva evaluación'}</button>
	</header>

	{#if mensaje}<div class="alert alert-success alert-dismissible fade show" role="alert"><i class="bi bi-check-circle-fill me-2"></i>{mensaje}<button class="btn-close" type="button" aria-label="Cerrar" onclick={() => mensaje = ''}></button></div>{/if}
	{#if mostrarFormulario}
		<section class="card border-0 shadow-sm mb-4"><div class="card-body p-4"><h3 class="h5 fw-bold mb-3">Registro de rúbrica</h3><form onsubmit={guardar}><div class="row g-3">
			<div class="col-md-6"><label class="form-label" for="practica">Práctica asignada</label><select id="practica" class="form-select" bind:value={nueva.practica_id}>{#each $practicasStore as p}<option value={p.id}>{p.estudiante_nombre} — {p.empresa_nombre}</option>{/each}</select></div>
			<div class="col-md-6"><label class="form-label" for="tipo">Momento de evaluación</label><select id="tipo" class="form-select" bind:value={nueva.tipo}><option>Evaluación de Medio Término</option><option>Evaluación Final</option></select></div>
			<div class="col-md-4"><label class="form-label" for="tecnica">Competencia técnica (1–5)</label><input id="tecnica" class="form-control" type="number" min="1" max="5" step="0.1" bind:value={nueva.competencia_tecnica} /></div>
			<div class="col-md-4"><label class="form-label" for="actitud">Competencia actitudinal (1–5)</label><input id="actitud" class="form-control" type="number" min="1" max="5" step="0.1" bind:value={nueva.competencia_actitudinal} /></div>
			<div class="col-md-4"><label class="form-label" for="puntualidad">Puntualidad (1–5)</label><input id="puntualidad" class="form-control" type="number" min="1" max="5" step="0.1" bind:value={nueva.puntualidad} /></div>
			<div class="col-12"><label class="form-label" for="observaciones">Observaciones</label><textarea id="observaciones" class="form-control" rows="3" placeholder="Fortalezas y oportunidades de mejora" bind:value={nueva.observaciones}></textarea></div>
			<div class="col-12 text-end"><button class="btn btn-success" type="submit"><i class="bi bi-save me-2"></i>Guardar evaluación</button></div>
		</div></form></div></section>
	{/if}

	<section class="card border-0 shadow-sm"><div class="card-header bg-white p-3 d-flex flex-column flex-md-row justify-content-between gap-3"><div><h3 class="h5 mb-1">Historial de evaluaciones</h3><small class="text-muted">Calificación final calculada sobre 5.0.</small></div><div class="input-group" style="max-width: 360px"><span class="input-group-text"><i class="bi bi-search"></i></span><input class="form-control" type="search" aria-label="Buscar evaluación" placeholder="Buscar estudiante o tipo" bind:value={busqueda}></div></div>
		<div class="table-responsive"><table class="table table-hover align-middle mb-0"><thead class="table-light"><tr><th class="ps-4">Estudiante</th><th>Tipo</th><th>Competencias</th><th>Nota final</th><th>Evaluador</th><th>Estado</th></tr></thead><tbody>{#each evaluacionesFiltradas as e}<tr><td class="ps-4 fw-semibold">{e.estudiante_nombre}<small class="d-block text-muted">{e.fecha}</small></td><td>{e.tipo}</td><td><small>Técnica: {e.competencia_tecnica} · Actitud: {e.competencia_actitudinal} · Puntualidad: {e.puntualidad}</small></td><td><span class="badge bg-primary fs-6">{e.calificacion_final}</span></td><td>{e.evaluador}</td><td><span class="badge bg-success-subtle text-success border border-success-subtle">{e.estado}</span></td></tr>{:else}<tr><td colspan="6" class="text-center text-muted py-4">No hay evaluaciones que coincidan con la búsqueda.</td></tr>{/each}</tbody></table></div>
	</section>
</div>
