setInterval(
    function(){
        if ($("#start_autobet").is( ":visible" )){
            console.warn("START")
            $("#start_autobet").click()
        }
    }, 5000
)