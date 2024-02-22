<script>
    import * as d3 from "d3";

    // Receive plot LineChartData as prop.
    export let LineChartData;
    export let GroupName;

    // Normalize the case of groups for comparison
    $: normalizedGroups = groups.map(g => g.toLowerCase());

    // Reactively update the index based on groupname, ensuring case-insensitive comparison
    $: pass_index = normalizedGroups.indexOf(GroupName);

    $: if (pass_index !== -1) {
        LineVisibilityFunction(pass_index);
    }
    // The chart dimensions and margins as optional props.
    export let width = 1000;
    export let height = 400;
    export let marginTop = 60;
    export let marginRight = 30;
    export let marginBottom = 60;
    export let marginLeft = 60;

    const startDate = d3.timeParse("%Y-%m")("2010-01");
    const endDate = d3.timeParse("%Y-%m")("2024-02");

    let lastAction = ""; // Possible values: "button", "groupname"
    let pass_index = -1; // Assuming this gets updated on button click
    let groupNameIndex = -1; // This should be updated when `groupname` changes

    $: groupNameIndex = GroupName ? normalizedGroups.indexOf(GroupName.toLowerCase()) : -1;

    $: if (lastAction === "button") {
        console.log(lastAction)
        lineVisibility = lineVisibility.map((_, i) => i === pass_index);
    } else if (lastAction === "GroupName") {
        console.log(lastAction)
        lineVisibility = lineVisibility.map((_, i) => i === groupNameIndex);
    }

    function handleButtonClick(index) {
        pass_index = index;
        lastAction = "button";
        // Optionally toggle visibility or directly set it
        // lineVisibility[index] = !lineVisibility[index]; // For toggling
    }

    $: if (GroupName) {
        lastAction = "GroupName";
        // groupNameIndex is already being updated reactively
    }

    let lineVisibility = Array(36).fill(false);
    $: lineVisibility = lineVisibility.map((_, i) => i === pass_index);
    let groups = ['2NE1', '4minute', 'After School', 'Apink', 'Brave Girls', 'Brown Eyed Girls', 'Davichi', "f(x)", "Girl's Day", "Girl's Generation", 'Kara', 'miss A', 'Secret', 'SISTAR', 'T-ara', 'Wonder Girls', 'AOA', 'BLACKPINK', 'EXID', 'GFRIEND', 'I.O.I', 'MAMAMOO', 'MOMOLAND', 'OH MY GIRL', 'Red Velvet', 'TWICE', '(G)I-DLE', 'aespa', 'ITZY', 'IVE', 'IZ*ONE', 'Kep1er', 'LE SSERAFIM', 'NewJeans', 'NMIXX', 'STAYC']


    const colorCodes = [
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78',
        '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7',
        '#dbdb8d', '#9edae5', '#393b79', '#5254a3', '#6b6ecf', '#9c9ede',
        '#637939', '#8ca252', '#b5cf6b', '#cedb9c', '#8c6d31', '#bd9e39',
        '#e7ba52', '#e7cb94', '#843c39', '#ad494a', '#d6616b', '#e7969c',
    ]

    // Create the x (horizontal position) scale.
    const xScale = d3.scaleTime()
        .domain([startDate, endDate])
        .range([marginLeft, width - marginRight]);

    // Create the y (vertical position) scale.
    const yScale = d3.scaleLinear()
        .domain([0, 100])
        .range([height - marginBottom, marginTop]);

    // Creating lines
    let lines = []
    for (let i = 0; i < 36; i++) {
        const line = d3
            .line()
            .x((d) => xScale(new Date(d.Month)))
            .y((d) => yScale(d[groups[i]]));
        lines.push(line)
    }


    function LineVisibilityFunction(index) {
        const visibleCount = countTrue(lineVisibility);

        if (visibleCount >= 3) {
            // If maximum limit is reached and the clicked line is already visible, hide it
            if (lineVisibility[index]) {
                lineVisibility[index] = false;
            }
        } else {
            // If maximum limit is not reached, toggle the visibility of the clicked line
            lineVisibility[index] = !lineVisibility[index];
        }
    }

    // count number of true values
    function countTrue(array) {
        return array.reduce((acc, currentValue) => acc + (currentValue ? 1 : 0), 0);
    }
</script>

{#each Array(36) as _, index}
    <button
            on:click={() => handleButtonClick(index)}
            style="background-color: {lineVisibility[index] ? colorCodes[index] : ''}; #E5E7E9
    color: {lineVisibility[index] ? 'white' : 'black'}
    border-radius: 50%; /* This will make the button round */
    padding: 10px; /* Adjust padding as needed */
  "
    >
        {groups[index]}
    </button>
{/each}


<svg
        {width}
        {height}
        viewBox="0 0 {width} {height}"
        style:max-width="100%"
        style:height="auto"
>

    <!-- Title -->
    <text
            x={(width - marginLeft - marginRight) / 2 + marginLeft}
            y={marginTop / 2}
            fill="currentColor"
            font-family="Trebuchet MS"
            font-size="24px"
            text-anchor="middle"
    >
        Popularity of Kpop Girl Groups
    </text>

    <!-- x axis Title -->
    <text
            x={(width - marginLeft - marginRight) / 2 + marginLeft}
            y={height}
            fill="currentColor"
            font-family="Trebuchet MS"
            font-size="15px"
            text-anchor="middle"
    >
        Month, Year
    </text>

    <!-- y axis Title -->
    <text
            x={(width - marginLeft - marginRight) / 2 + marginLeft -150}
            y={-470}
            fill="currentColor"
            font-family="Trebuchet MS"
            font-size="15px"
            text-anchor="middle"
            transform="rotate(-90, {(width - marginLeft - marginRight) / 2 + marginLeft}, {marginTop / 2})"
    >
        Trend
    </text>


    <!-- X-Axis -->
    <g transform="translate(0,{height - marginBottom})">
        <line stroke="currentColor" stroke-width=2 stroke-opacity="0.3" x1={marginLeft - 6} x2={width}/>

        {#each xScale.ticks() as tick}
            <!-- X-Axis Ticks -->
            <line
                    stroke="currentColor"
                    stroke-opacity="0.3"
                    x1={xScale(tick)}
                    x2={xScale(tick)}
                    y1={0}
                    y2={6}
            />

            <!-- X-Axis Tick Labels -->
            <text fill="currentColor" font-family='Trebuchet MS' text-anchor="middle" x={xScale(tick)} y={22}>
                {tick.getFullYear()}
            </text>
        {/each}
    </g>

    <!-- Y-Axis and Grid Lines -->
    <g transform="translate({marginLeft},0)">
        {#each [0, 25, 50, 75, 100] as tick}
            {#if tick !== 0}
                <!--
                  Grid Lines.
                  Note: First line is skipped since the x-axis is already present at 0.
                -->
                <line
                        stroke="currentColor"
                        stroke-opacity="0.1"
                        x1={0}
                        x2={width - marginLeft}
                        y1={yScale(tick)}
                        y2={yScale(tick)}
                />

                <!--
                  Y-Axis Ticks.
                  Note: First tick is skipped since the x-axis already acts as a tick.
                -->
                <line
                        stroke="currentColor"
                        stroke-opacity="0.1"
                        x1={0}
                        x2={-6}
                        y1={yScale(tick)}
                        y2={yScale(tick)}
                />
            {/if}

            <!-- Y-Axis Tick Labels -->
            <text
                    fill="currentColor"
                    text-anchor="end"
                    dominant-baseline="middle"
                    font-family='Trebuchet MS'
                    x={-9}
                    y={yScale(tick)}
            >
                {tick}
            </text>
        {/each}
    </g>

    {#each lines as line, index}
        <path
                fill="none"
                stroke={colorCodes[index % colorCodes.length]}
                stroke-width="3"
                d={lines[index](LineChartData)}
                style:opacity={lineVisibility[index] ? 1 : 0}
        />
    {/each}
</svg>