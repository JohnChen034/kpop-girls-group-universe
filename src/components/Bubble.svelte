<script>
    import * as d3 from 'd3';
    import {onMount} from 'svelte';
    import LineChart from './LineChart.svelte';

    export let data;
    export let LineChartData;

    console.log('LineChartData loaded:', LineChartData);

    let GroupName;

    let groups = [];

    const prepareData = () => {
        data.forEach(group => {
            groups.push({
                name: group.name,
                debut: group.debut,
                // info: group.info,
                url: group.url, // Include the URL in the data preparation
                singles: group.singles,
                albums: group.albums,
                members: group.members,
                generation: group.generation
                // specificInfo: group.specificInfo
            });
        });
    };


    onMount(() => {
        prepareData();
        // Correct position calculation to avoid overlap
        groups = groups.map((group, _, arr) => {
            const sameYearCountBefore = arr.filter(d => d.debut === group.debut && d.name < group.name).length;
            return {...group, position: sameYearCountBefore};
        });
        drawChart();
    });

    const drawChart = () => {
        const svgWidth = 1000;
        const svgHeight = 500;
        const margin = {top: 20, right: 20, bottom: 30, left: 40};
        const imageSize = 40; // Define a fixed size for images
        const detailsSection = d3.select("#details");


        // Create SVG container
        const svg = d3.select('#chart')
            .attr('viewBox', `0 0 ${svgWidth} ${svgHeight}`)
            .attr('preserveAspectRatio', 'xMidYMid meet');

        // Scale for the x-axis (debut year)
        const xScale = d3.scaleLinear()
            .domain([2000, 2023]) // Fixed domain for years 2000 to 2023
            .range([margin.left, svgWidth - margin.right]);
        const generations = [
            {year: 2006, label: "Generation 2"},
            {year: 2012, label: "Generation 3"},
            {year: 2018, label: "Generation 4"}
        ];
        generations.forEach(generation => {
            svg.append('line')
                .attr('x1', xScale(generation.year))
                .attr('x2', xScale(generation.year))
                .attr('y1', margin.top)
                .attr('y2', svgHeight - margin.bottom)
                .attr('stroke', '#007bff')
                .attr('stroke-dasharray', '5,5')
                .style('fill', '#333');

            svg.append('text')
                .attr('x', xScale(generation.year))
                .attr('y', margin.top - 5) // Position the label slightly above the top of the line
                .attr('text-anchor', 'middle') // Center the text on the line
                .text(generation.label);
        });
        // Calculate y-offset for overlapping groups
        const yOffset = 40; // Adjust this value as needed

        const tooltip = d3.select("#tooltip");

        const enlargedSize = 60; // Enlarged size for images on hover
        const groupSelection = svg.selectAll('.group')
            .data(groups)
            .enter().append('g')
            .attr('class', 'group')
            .attr('transform', d => `translate(${xScale(d.debut) - imageSize / 2}, ${svgHeight / 2 - imageSize / 2 + (d.position * yOffset)})`);

// Inside drawChart function, where you append images and handle hover events
        groupSelection.append('image')
            .attr('xlink:href', d => d.url)
            .attr('width', imageSize)
            .attr('height', imageSize)
            .attr('x', -imageSize / 2)
            .attr('y', -imageSize / 2)
            .on('click', (event, d) => {
                // Update the details section with the specificInfo of the clicked group
                GroupName = d.name.toLowerCase();
                console.log(GroupName)

                detailsSection.style('opacity', 0)
                setTimeout(() => {
                    detailsSection
                        .html(`
                            <strong>Name:</strong> ${d.name}<br/>
                            <strong>Debut year:</strong> ${d.debut}<br/>
                            <p><strong>singles:</strong> ${d.singles}</p><br/>
                            <p><strong>albums:</strong> ${d.albums || 'No specific information provided.'}</p>
                            `)
                        .style('opacity', 1); // Fade in by setting opacity back to 1
                }, 500);
            })
            .on('mouseover', function (event, d) {
                d3.select(this)
                    .transition()
                    .duration(300) // Duration of the enlarge transition
                    .attr('width', enlargedSize)
                    .attr('height', enlargedSize)
                    .attr('x', -enlargedSize / 2) // Adjust the x and y to keep the image centered
                    .attr('y', -enlargedSize / 2);
                tooltip.transition()
                    .duration(200)
                    .style("opacity", .9);
                tooltip.html(`
                    <strong>Group Name:</strong> ${d.name}<br/>
                    <strong>Debut year: </strong> ${d.debut}<br/>
                    <strong>Generation: </strong> ${d.generation}<br/>

                    `)
                    .style("left", (event.pageX) + "px")
                    .style("top", (event.pageY - 28) + "px");
                // Tooltip logic remains unchanged, ensure it's set to show the tooltip without hiding it on mouseout
            })

            .on('mouseout', function (event, d) {
                    d3.select(this)
                        .transition()
                        .duration(300) // Duration of the shrink transition
                        .attr('width', imageSize)
                        .attr('height', imageSize)
                        .attr('x', -imageSize / 2) // Correctly adjust back the x and y to keep the image centered
                        .attr('y', -imageSize / 2);
                    tooltip.transition()
                        .duration(500)
                        .style("opacity", 0);
                }
            );

        // Draw the x-axis
        const xAxis = d3.axisBottom(xScale).tickFormat(d3.format("d")).ticks(23);
        svg.append("g")
            .attr("transform", `translate(0,${svgHeight - margin.bottom})`)
            .call(xAxis)
            .attr("color", "black");
    };
</script>

<main>

    <svg id="chart"></svg>

    <div id="tooltip" class="tooltip" style="opacity: 0;"></div>

    <div id="details" class="details"></div>

    <LineChart LineChartData="{LineChartData}" GroupName="{GroupName}"/>
</main>

<style>
    svg {
        display: block;
        margin: 0 auto;
        background-color: #f9f9f9;
    }

    .details {
        padding: 10px;
        margin-top: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    text {
        font-size: 12px;
        font-family: Arial, sans-serif;
    }

    .tooltip {
        position: absolute;
        text-align: center;
        padding: 10px;
        background: white;
        border: 1px solid #ccc;
        border-radius: 5px;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.3s;
    }

    .details {
        transition: opacity 0.5s ease-in-out;
        opacity: 0; /* Start invisible */
    }
</style>
