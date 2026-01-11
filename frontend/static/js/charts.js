document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("progressChart");

    if (ctx) {
        new Chart(ctx, {
            type: "line",
            data: {
                labels: ["Week 1", "Week 2", "Week 3", "Week 4"],
                datasets: [{
                    label: "Skill Improvement",
                    data: [2, 4, 6, 8],
                }]
            }
        });
    }
});
