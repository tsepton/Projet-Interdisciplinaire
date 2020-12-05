<script>
  export let line;

  console.log(line);
</script>

<div>Destination : <b>{line.destination.fr}</b></div>
<div>
  Direction :
  <b>{#if line.direction.toLowerCase() === 'city'}Ville{:else}Banlieue{/if}</b>
  <p>
    Délais prévus pour le prochaine train passant par cet arrêt dans cette
    direction
  </p>
</div>
