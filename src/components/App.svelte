<script>
    import {onMount} from "svelte";
    import Bubble from './Bubble.svelte';

    let data;
    let LineChartData;

    onMount(async () => {
        const res = await fetch('kpop_data.json');
        data = await res.json();

        const res2 = await fetch('kpop_trend.json');
        LineChartData = await res2.json();

        console.log('Data loaded:', data);
        console.log('LineChartData loaded:', LineChartData);
    });


</script>

<main>
    <h1>Kpop Girls Group Universe!</h1>
    <!--    since fetch needs operation time-->
    {#if data}
        {#if LineChartData}
            <Bubble data={data} LineChartData={LineChartData}/>
        {/if}
    {/if}


</main>

<style>
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