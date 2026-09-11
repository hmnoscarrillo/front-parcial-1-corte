<script>
	const anioActual = 2026;
</script>

<footer class="bg-dark text-white pt-4 pb-3 mt-auto border-top border-secondary shadow">
	<div class="container-fluid px-4">
		<div class="row gy-4 mb-3">
			<!-- Columna 1: Datos del Proyecto -->
			<div class="col-12 col-md-4">
				<div class="d-flex align-items-center gap-2 mb-2">
					<i class="bi bi-mortarboard-fill text-warning fs-5"></i>
					<h5 class="fw-bold mb-0 text-white">SGPP - Evidencia 40%</h5>
				</div>
				<p class="text-white-50 small mb-2">
					Sistema integral para la gestión y seguimiento de prácticas profesionales y empresariales con control de acceso jerárquico RBAC.
				</p>
				<div class="d-flex gap-2 flex-wrap">
					<span class="badge bg-secondary">SvelteKit 2</span>
					<span class="badge bg-secondary">Svelte 5 Runes</span>
					<span class="badge bg-primary">Bootstrap 5.3</span>
					<span class="badge bg-info text-dark">Sin CSS personalizado</span>
				</div>
			</div>

			<!-- Columna 2: Sustentación y Preguntas Docente -->
			<div class="col-12 col-md-4">
				<h6 class="fw-bold text-uppercase text-warning mb-2 small">
					<i class="bi bi-patch-question me-1"></i> Sustentación y Evaluación
				</h6>
				<p class="text-white-50 small mb-2">
					Diseñado conforme a los estándares de Usabilidad Web (Electiva I). Cada vista cuenta con formularios semánticos, componentes modulares y tablas responsivas preparadas para preguntas individuales de sustentación.
				</p>
				<div class="card bg-secondary bg-opacity-25 border-secondary p-2">
					<small class="text-light fw-medium">
						<i class="bi bi-shield-check text-success me-1"></i>
						Jerarquía RBAC: 1=Admin, 2=Coordinador, 3=Profesor, 4=Estudiante
					</small>
				</div>
			</div>

			<!-- Columna 3: Enlaces Rápidos y Navegación -->
			<div class="col-12 col-md-4">
				<h6 class="fw-bold text-uppercase text-warning mb-2 small">
					<i class="bi bi-link-45deg me-1"></i> Módulos Principales
				</h6>
				<div class="row g-1 small">
					<div class="col-6">
						<ul class="list-unstyled mb-0">
							<li><a href="/" class="text-white-50 text-decoration-none hover-white">→ Dashboard</a></li>
							<li><a href="/programas" class="text-white-50 text-decoration-none hover-white">→ Programas</a></li>
							<li><a href="/empresas" class="text-white-50 text-decoration-none hover-white">→ Empresas</a></li>
							<li><a href="/estudiantes" class="text-white-50 text-decoration-none hover-white">→ Estudiantes</a></li>
							<li><a href="/tutores" class="text-white-50 text-decoration-none hover-white">→ Tutores</a></li>
						</ul>
					</div>
					<div class="col-6">
						<ul class="list-unstyled mb-0">
							<li><a href="/convenios" class="text-white-50 text-decoration-none hover-white">→ Convenios</a></li>
							<li><a href="/practicas" class="text-white-50 text-decoration-none hover-white">→ Prácticas</a></li>
							<li><a href="/seguimientos" class="text-white-50 text-decoration-none hover-white">→ Seguimientos</a></li>
							<li><a href="/evaluaciones" class="text-white-50 text-decoration-none hover-white">→ Evaluaciones</a></li>
							<li><a href="/seguridad" class="text-white-50 text-decoration-none hover-white">→ Seguridad RBAC</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>

		<hr class="border-secondary my-3" />

		<!-- Subfooter de Derechos y Créditos -->
		<div class="d-flex flex-column flex-sm-row justify-content-between align-items-center gap-2 text-white-50 small">
			<div>
				© {anioActual} Universidad • Facultad de Ingeniería • Parcial 1er Corte (40%)
			</div>
			<div class="d-flex align-items-center gap-3">
				<span><i class="bi bi-code-slash text-warning me-1"></i> HTML5 Semántico + Svelte + JS</span>
				<span><i class="bi bi-check-circle-fill text-success me-1"></i> Totalmente Responsivo</span>
			</div>
		</div>
	</div>
</footer>
