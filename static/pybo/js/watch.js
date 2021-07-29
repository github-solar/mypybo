//디지털 시계 구현 자바스크립트
setInterval(mywatch, 1000)

function mywatch(){
    var date = new Date()
    var now = date.toLocaleTimeString()
    document.getElementById("demo").innerHTML = now;

}