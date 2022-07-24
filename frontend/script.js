function valNumber() {
    let p = document.getElementById("principal").value;
    if (p <= 0) {
        alert("Enter a positive number");
        p.focus();
        return false;
    }
    return true;    
}

function compute() {
    var principal = document.getElementById("principal").value;
    var rate = document.getElementById("rate").value;
    var years = document.getElementById("years").value;
    var interest = principal * years * rate / 100;
    var amount = interest;
    // compound return p * (1+i)^n
    // var amount = (principal * Math.pow(1+rate/100, years)).toFixed(2);
    var year = new Date().getFullYear()+parseInt(years);
    var result ="If you deposit <span class=\"yellow_bg\">"+principal+",</span><br>at an interest rate of <span class=\"yellow_bg\">"+rate+"%,</span><br>you will receive an amount of <span class=\"yellow_bg\">"+amount+",</span><br>in the year <span class=\"yellow_bg\">"+year+".</span<br>"

    document.getElementById("result").innerHTML= result;
}

// Update rate from range input
function updateRate() {
    var rateval = document.getElementById("rate").value;
    document.getElementById("rate_val").innerText=rateval + "%";
}

