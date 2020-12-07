<script>
  export let line;
  export let delay;

  let delayFormatted = convertNumToTime(delay);
  function convertNumToTime(delay) {
    // Check sign of given number
    let sign = delay >= 0 ? 1 : -1;

    // Set positive value of number of sign negative
    const number = delay * sign;

    // Separate the int from the decimal part
    let hour = Math.floor(number);
    let decpart = number - hour;

    let min = 1 / 60;
    // Round to nearest minute
    decpart = min * Math.round(decpart / min);

    let minute = Math.floor(decpart * 60) + "";

    // Add padding if need
    if (minute.length < 2) minute = "0" + minute;

    // Add Sign in final result
    sign = sign == 1 ? "" : "-";

    // Concate hours and minutes
    const time = sign + hour + ":" + minute;

    return time;
  }
</script>

<div>Destination : <b>{line.destination.fr}</b></div>
<div>
  Ligne en direction de la {#if line.direction.toLowerCase() === 'city'}ville.{:else}banlieue.{/if}
</div>
{#if delay}
  Le retard prédit du prochain train passant par cette station dans cette
  direction est de {delayFormatted}m.
{/if}
