<script>
	let { items = [] } = $props();
</script>

<nav aria-label="breadcrumb" class="my-3">
	<ol class="breadcrumb mb-0 bg-white px-3 py-2 rounded-3 shadow-sm border small">
		<li class="breadcrumb-item">
			<a href="/" class="text-decoration-none text-primary">
				<i class="bi bi-house-door-fill me-1"></i>Inicio
			</a>
		</li>
		{#each items as item, index}
			{#if index === items.length - 1}
				<li class="breadcrumb-item active text-secondary fw-semibold" aria-current="page">
					{item.label}
				</li>
			{:else}
				<li class="breadcrumb-item">
					<a href={item.href} class="text-decoration-none text-primary">
						{item.label}
					</a>
				</li>
			{/if}
		{/each}
	</ol>
</nav>
