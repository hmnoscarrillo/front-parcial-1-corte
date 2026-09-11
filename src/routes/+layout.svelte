<script>
	import Header from '$lib/components/Header.svelte';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<title>Sistema de Gestión de Prácticas Profesionales</title>
</svelte:head>

<!-- Componente Encabezado Institucional -->
<Header />

<!-- Componente Menú de Navegación Responsivo -->
<Navbar />

<!-- Contenedor Principal Dinámico (Slot de SvelteKit) -->
<main class="flex-grow-1">
	{@render children()}
</main>

<!-- Componente Pie de Página -->
<Footer />
