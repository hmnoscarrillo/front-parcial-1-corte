<script>
	let {
		title = 'Métrica',
		value = '0',
		icon = 'bi-bar-chart',
		color = 'primary',
		description = '',
		trend = ''
	} = $props();
</script>

<div class="col-12 col-sm-6 col-xl-3">
	<div class="card border-0 shadow-sm rounded-3 h-100 border-start border-4 border-{color}">
		<div class="card-body p-3">
			<div class="d-flex align-items-center justify-content-between">
				<div>
					<p class="text-uppercase text-muted fw-bold mb-1" style="font-size: 0.75rem;">
						{title}
					</p>
					<h3 class="fw-bold mb-0 text-dark">{value}</h3>
				</div>
				<div class="bg-{color}-subtle text-{color} rounded-circle p-3 d-flex align-items-center justify-content-center" style="width: 48px; height: 48px;">
					<i class="bi {icon} fs-4"></i>
				</div>
			</div>
			{#if description || trend}
				<div class="mt-2 pt-2 border-top d-flex align-items-center justify-content-between small text-muted">
					<span>{description}</span>
					{#if trend}
						<span class="badge bg-success-subtle text-success fw-medium">{trend}</span>
					{/if}
				</div>
			{/if}
		</div>
	</div>
</div>
