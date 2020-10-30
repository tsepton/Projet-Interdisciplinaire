<script>
import { mapbox } from "../lib/mapbox";


//   import { getContext } from "svelte";
//   import { key } from "../lib/mapbox.js";

//   const { getMap } = getContext(key);
//   const map = getMap();

  export let lines;
//   export let points;

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

    #line-select {
        display: inline-block;
        margin: 20px 0 0 30px;
        padding: 5px 15px;
        width: 100px;
    }

</style>

<div class="content">  
    <div class="dropdown-filter">
        <label class="dropdwn" for="line-select">Filter</label>
        <select name="lines" id="line-select">
            {#each lines.features as lprop}
                <option value="{lprop.properties.LIGNE}">{lprop.properties.LIGNE}</option>
            {/each}
        </select>
    </div>
</div>