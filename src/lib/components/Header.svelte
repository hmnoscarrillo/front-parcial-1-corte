<script>
	import { rolActivoStore, initialRoles } from '$lib/data/mockData.js';

	let rolesDisponibles = [
		{ id: 1, nombre: 'Administrador', nivel_jerarquia: 1, usuario: 'Ivan Carrillo (Admin Central)', icono: 'bi-shield-check' },
		{ id: 2, nombre: 'Coordinador', nivel_jerarquia: 2, usuario: 'Lic. Claudia Morales (Coordinadora)', icono: 'bi-person-badge' },
		{ id: 3, nombre: 'Profesor', nivel_jerarquia: 3, usuario: 'Dr. Fernando Jaramillo (Docente Tutor)', icono: 'bi-mortarboard' },
		{ id: 4, nombre: 'Estudiante', nivel_jerarquia: 4, usuario: 'Mateo Alejandro Pérez (Estudiante)', icono: 'bi-person' }
	];

	function cambiarRol(event) {
		const seleccionado = rolesDisponibles.find((r) => r.id === Number(event.target.value));
		if (seleccionado) {
			rolActivoStore.set(seleccionado);
		}
	}
</script>

<header class="bg-primary text-white py-3 shadow-sm border-bottom">
	<div class="container-fluid px-4">
		<div class="row align-items-center gy-2">
			<!-- Branding & Título Institucional -->
			<div class="col-12 col-md-7 d-flex align-items-center gap-3">
				<div class="bg-white text-primary rounded-circle p-2 d-flex align-items-center justify-content-center shadow-sm" style="width: 48px; height: 48px;">
					<i class="bi bi-briefcase-fill fs-4"></i>
				</div>
				<div>
					<div class="d-flex align-items-center gap-2 flex-wrap">
						<h1 class="h4 mb-0 fw-bold tracking-tight text-white">SGPP - Prácticas Profesionales</h1>
						<span class="badge bg-warning text-dark fw-semibold">Evidencia 40%</span>
						<span class="badge bg-white text-primary fw-medium">SvelteKit + Bootstrap</span>
					</div>
					<p class="mb-0 text-white-50 small">
						Vicerrectoría Académica • Sistema de Prácticas y Control de Acceso Jerárquico (RBAC)
					</p>
				</div>
			</div>

			<!-- Perfil Activo y Selector de Rol RBAC -->
			<div class="col-12 col-md-5 d-flex justify-content-md-end align-items-center gap-2">
				<div class="bg-primary-subtle text-dark px-3 py-1 rounded-3 border d-flex align-items-center gap-2 shadow-sm">
					<i class="bi {$rolActivoStore.icono} text-primary fs-5"></i>
					<div class="text-start">
						<div class="fw-bold small lh-1">{$rolActivoStore.usuario}</div>
						<small class="text-muted" style="font-size: 0.75rem;">
							Jerarquía: Nivel {$rolActivoStore.nivel_jerarquia} ({$rolActivoStore.nombre})
						</small>
					</div>
				</div>

				<!-- Selector interactivo de simulación -->
				<div class="d-flex flex-column align-items-end">
					<label for="selector-rol" class="visually-hidden">Cambiar Rol</label>
					<select
						id="selector-rol"
						class="form-select form-select-sm bg-light fw-medium border-0 shadow-sm"
						value={$rolActivoStore.id}
						onchange={cambiarRol}
						aria-label="Seleccionar rol de simulación"
					>
						{#each rolesDisponibles as r}
							<option value={r.id}>
								Rol: {r.nombre} (Nivel {r.nivel_jerarquia})
							</option>
						{/each}
					</select>
				</div>
			</div>
		</div>
	</div>
</header>
