<script>
	export let version;
	import Map from "./components/Map.svelte";
	import MapMarker from './components/MapMarker.svelte';
</script>

<main>

	<h1>Projet Interdisciplinaire: v{version}</h1>

	<div class='mapbox'>
		<Map lat={50.842912} lon={4.377492} zoom={10.9}>
			<MapMarker lat={50.465856} lon={4.857599} label="UNamur"/>
		</Map>
	</div>

</main>

<style>


	.mapbox {
		height: 75vh;
		margin: 1rem;
	}


	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>