var state = [];
state.length = 63;
state.fill(-1);

const DEBUG = 1;


var e0 = 0.38
var s0 = 2.41

econv = [
    //[4.5, 2.5, -2.5, -4.5],
    [7, 5, 0, -2], //p1
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [7, 5, 0, -2], //p2
    [-7, -5, 0, 2],
    [6, 4, 0, -2],
    [7, 5, 0, -2],
    [-8, -6, 0, 2],
    [8, 6, 0, -2],
    [8, 6, 0, -1],
    [7, 5, 0, -3],
    [8, 6, 0, -1],
    [-7, -5, 0, 2],
    [-7, -5, 0, 1],
    [-6, -4, 0, 2],
    [6, 4, 0, -1],
    [0, 0, 0, 0],
    [0, 0, 0, 0], //p3
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-8, -6, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-10, -8, 0, 1],
    [-5, -4, 0, 1],
    [0, 0, 0, 0], //p4
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0], //p5
    [0, 0, 0, 0],
    [-9, -8, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0], //p6
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

socv = [
    [0, 0, 0, 0], //p1
    [-8, -6, 0, 2],
    [7, 5, 0, -2],
    [-7, -5, 0, 2],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [7, 5, 0, -2],
    [0, 0, 0, 0], //p2
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [-6, -4, 0, 2], //p3
    [7, 6, 0, -2],
    [-5, -4, 0, 2],
    [0, 0, 0, 0],
    [8, 4, 0, -2],
    [-7, -5, 0, 2],
    [-7, -5, 0, 3],
    [6, 4, 0, -3],
    [6, 3, 0, -2],
    [-7, -5, 0, 3],
    [-9, -7, 0, 2],
    [-8, -6, 0, 2],
    [7, 6, 0, -2],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [-7, -4, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [7, 5, 0, -3], //p4
    [-9, -6, 0, 2],
    [-8, -6, 0, 2],
    [-8, -6, 0, 2],
    [-6, -4, 0, 2],
    [-8, -6, 0, 2],
    [-7, -5, 0, 2],
    [-8, -6, 0, 2],
    [-5, -3, 0, 2],
    [-7, -5, 0, 2],
    [7, 5, 0, -2],
    [-6, -4, 0, 2],
    [-7, -5, 0, 2], //p5
    [-6, -4, 0, 2],
    [0, 0, 0, 0],
    [-7, -5, 0, 2],
    [-6, -4, 0, 2],
    [-7, -6, 0, 2], //p6
    [7, 6, 0, -2],
    [7, 5, 0, -2],
    [8, 6, 0, -2],
    [-8, -6, 0, 2],
    [-6, -4, 0, 2]
]

function upd() {
    var sumE = 0, sumS = 0

    for (var i = 0; i < 62; i++) {
        if (state[i] != -1) {
            sumE += econv[i][state[i]]
            sumS += socv[i][state[i]]
        }
    }

    if (DEBUG)
        console.log(sumE.toString() + ' ' + sumS.toString())

    var valE = sumE / 8.0
    var valS = sumS / 19.5

    valE += e0
    valS += s0

    valE = Math.round((valE + Number.EPSILON) * 100) / 100
    valS = Math.round((valS + Number.EPSILON) * 100) / 100

    document.getElementById('h4disp').innerHTML = 'Economic <span id="displayEcon">' + valE.toString() + '</span><span class="disp-sp">&nbsp;</span><span class="sep-disp"></span>Social <span id="displaySoc">' + valS.toString() + '</span>'
    document.getElementById('circ').setAttribute("cx", (valE * 5.0 + 50).toString())
    document.getElementById('circ').setAttribute("cy", (-valS * 5.0 + 50).toString())
}


document.getElementById('fileInput').addEventListener('change', function (e) {
    const file = e.target.files[0];
    
    if (file) {
        Papa.parse(file, {
            complete: function (results) {
                const data = results.data;
                
                if (data.length === 63) {
                    // Clear the existing state array
                    state = [];
                    
                    // Parse each answer from the CSV data
                    for (let i = 0; i < data.length; i++) {
                        const answer = parseInt(data[i][1]);
                        if (!isNaN(answer)) {
                            state.push(answer);
                        } else {
                            state.push(-1); // Handle missing or invalid values
                        }
                    }

                    console.log(state)
                    
                    // Update the UI or perform calculations
                    upd();
                }
            }
        });
    }
});

libright = 'Yellow libright'

function switchLibright() {
    if (libright == 'Yellow libright') {
        document.getElementById('switchLibright').innerHTML = 'Yellow libright'
        document.getElementById('libright').style = 'fill:rgb(192,154,236);'
        libright = 'Purple libright'
        setCookie('libright', 'Purple libright', 365 * 2)
    }
    else {
        document.getElementById('switchLibright').innerHTML = 'Purple libright'
        document.getElementById('libright').style = 'fill:rgb(245,244,113);'
        libright = 'Yellow libright'
        setCookie('libright', 'Yellow libright', 365 * 2)
    }
}

indicator = 'Big indicator'

function switchIndicator() {
    if (indicator == 'Big indicator') {
        document.getElementById('switchIndicator').innerHTML = 'Big indicator'
        document.getElementById('circ').setAttribute('r', '1')
        indicator = 'Tiny indicator'
    }
    else {
        document.getElementById('switchIndicator').innerHTML = 'Tiny indicator'
        document.getElementById('circ').setAttribute('r', '2.5')
        indicator = 'Big indicator'
    }
}