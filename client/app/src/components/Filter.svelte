<script>
import { mapbox } from "../lib/mapbox";

  export let lines;
  export let points;

</script>

<style>
    .content {
        display: flex;
        align-items:  center;
        justify-content: center;
        width: 100%;
    }

    .dropdown-filter {
        width: 100%;
    }

    .dropdwn {
        display: block;
        margin: auto;
        font-size: 20px;
        height: 30px;
        width: 75%;
        text-align: center;
        padding: 5px;
        background-color: var(--secondary);
        color: white;
    }

    #line-select, #stop-select {
        display: inline-block;
        margin: 20px 0 0 30px;
        padding: 5px 15px;
        min-width: 100px;
    }

</style>

<div class="content">  
    <div class="dropdown-filter">
        <label class="dropdwn" for="line-select">Filter of lines</label>
        <select name="lines" id="line-select">
            {#each lines.features as lprop}
                <option value="{lprop.properties.LIGNE}">{lprop.properties.LIGNE}</option>
            {/each}
        </select>
    </div>

    <div class="dropdown-filter">
        <label class="dropdwn" for="stop-select">Filter of stops</label>
        <select name="points" id="stop-select">
            {#each points.features as pprop}
                <option value="{pprop.properties.alpha_fr}">{pprop.properties.alpha_fr}</option>
            {/each}
        </select>
    </div>
</div>