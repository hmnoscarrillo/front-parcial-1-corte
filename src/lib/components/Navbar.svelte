<script>
	import { page } from '$app/state';

	// Control de colapso móvil con estado reactivo de Svelte
	let isNavOpen = $state(false);

	function toggleNav() {
		isNavOpen = !isNavOpen;
	}

	function closeNav() {
		isNavOpen = false;
	}

	const menuItems = [
		{ href: '/', label: 'Inicio', icon: 'bi-speedometer2' },
		{ href: '/programas', label: 'Programas', icon: 'bi-mortarboard' },
		{ href: '/empresas', label: 'Empresas', icon: 'bi-buildings' },
		{ href: '/estudiantes', label: 'Estudiantes', icon: 'bi-people' },
		{ href: '/tutores', label: 'Tutores', icon: 'bi-person-badge' },
		{ href: '/convenios', label: 'Convenios', icon: 'bi-file-earmark-text' },
		{ href: '/practicas', label: 'Prácticas', icon: 'bi-briefcase-fill', badge: 'Core' },
		{ href: '/seguimientos', label: 'Seguimientos', icon: 'bi-journal-check' },
		{ href: '/evaluaciones', label: 'Evaluaciones', icon: 'bi-star-half' },
		{ href: '/documentos', label: 'Documentos', icon: 'bi-folder2-open' },
		{ href: '/seguridad', label: 'Seguridad RBAC', icon: 'bi-shield-lock-fill' }
	];

	function isActive(href) {
		if (href === '/') {
			return page.url.pathname === '/';
		}
		return page.url.pathname.startsWith(href);
	}
</script>

<nav class="navbar navbar-expand-xl navbar-dark bg-dark sticky-top shadow-sm py-1">
	<div class="container-fluid px-4">
		<!-- Etiqueta del Menú para Móviles -->
		<a class="navbar-brand d-xl-none fw-bold fs-6 d-flex align-items-center gap-2" href="/">
			<i class="bi bi-grid-3x3-gap-fill text-warning"></i>
			<span>Navegación del Sistema</span>
		</a>

		<!-- Botón Hamburguesa Responsivo con Svelte -->
		<button
			class="navbar-toggler border-0 shadow-none"
			type="button"
			onclick={toggleNav}
			aria-controls="navbarPrincipal"
			aria-expanded={isNavOpen}
			aria-label="Abrir menú de navegación"
		>
			<span class="navbar-toggler-icon"></span>
		</button>

		<!-- Enlaces y Pestañas del Menú -->
		<div class="collapse navbar-collapse {isNavOpen ? 'show' : ''}" id="navbarPrincipal">
			<ul class="navbar-nav me-auto mb-2 mb-xl-0 flex-wrap gap-1">
				{#each menuItems as item}
					<li class="nav-item">
						<a
							class="nav-link px-2 py-1 rounded d-flex align-items-center gap-1 {isActive(item.href) ? 'active bg-primary text-white fw-bold shadow-sm' : 'text-light'}"
							href={item.href}
							onclick={closeNav}
						>
							<i class="bi {item.icon}"></i>
							<span>{item.label}</span>
							{#if item.badge}
								<span class="badge bg-warning text-dark ms-1 font-monospace" style="font-size: 0.65rem;">
									{item.badge}
								</span>
							{/if}
						</a>
					</li>
				{/each}
			</ul>

			<!-- Indicador de Navegación Rápida -->
			<div class="d-none d-xl-flex align-items-center gap-2 text-white-50 small ps-2 border-start border-secondary">
				<i class="bi bi-compass"></i>
				<span class="text-truncate" style="max-width: 180px;">Ruta: <code class="text-warning">{page.url.pathname}</code></span>
			</div>
		</div>
	</div>
</nav>
