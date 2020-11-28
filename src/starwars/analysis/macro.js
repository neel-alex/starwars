// INPUTS
const maximizers = ["Advantage", "Success", "Triumph", "Despair"];
const min_successes = 1;
const max_despairs = 0;

/* Convention:
    A dice result is a 4-tuple (length-4 array).
        * The first number is the number of successes (negative indicates failures).
        * The second number is the number of advantages (negative indicates threats).
        * The third number is the number of triumphs (non-negative only).
        * The fourth number is the negative of the number of despairs (non-positive only).
*/

/*
============================================
======= DATA FUNCTIONS AND VARIABLES =======
============================================
==== THERE IS NO LOGIC TO BE FOUND HERE ====
============================================
================== BEWARE ==================
============================================
*/
// output from pretty js adjacency
// each of these gives, for a result on a given dice, the possible sets of potential adjacent faces.
const b = JSON.parse('{"0,0,0,0": [[[0, 1, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]], [[0, 1, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]], "0,1,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0]]], "1,0,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0]]], "1,1,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]], "0,2,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]]}');
const a = JSON.parse('{"2,0,0,0": [[[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]], "1,0,0,0": [[[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]], "0,1,0,0": [[[2, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], [[0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]], [[0, 2, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]], "1,1,0,0": [[[2, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]], "0,0,0,0": [[[0, 2, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]], "0,2,0,0": [[[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]]}');
const p = JSON.parse('{"1,0,1,0": [[[1, 0, 0, 0], [2, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]]], "1,0,0,0": [[[1, 0, 1, 0], [2, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]], [[0, 2, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]], "2,0,0,0": [[[1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], [[1, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]], "0,1,0,0": [[[1, 0, 1, 0], [2, 0, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]], "1,1,0,0": [[[1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 2, 0, 0], [2, 0, 0, 0]], [[1, 1, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]], [[2, 0, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]], "0,2,0,0": [[[1, 0, 1, 0], [1, 1, 0, 0], [2, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]], [[1, 1, 0, 0], [0, 2, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]], "0,0,0,0": [[[1, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [2, 0, 0, 0]]]}');
const s = JSON.parse('{"0,0,0,0": [[[-1, 0, 0, 0], [0, -1, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0]], [[-1, 0, 0, 0], [0, -1, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0]]], "-1,0,0,0": [[[0, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0], [0, -1, 0, 0]], [[0, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0], [0, -1, 0, 0]]], "0,-1,0,0": [[[0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0]], [[0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0]]]}');
const d = JSON.parse('{"-2,0,0,0": [[[0, -1, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0]]], "0,-1,0,0": [[[-2, 0, 0, 0], [-1, 0, 0, 0], [0, -2, 0, 0]], [[-2, 0, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0]], [[-1, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0]]], "0,0,0,0": [[[-2, 0, 0, 0], [0, -2, 0, 0], [-1, -1, 0, 0]]], "0,-2,0,0": [[[0, 0, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0]]], "-1,0,0,0": [[[0, -1, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0]]], "-1,-1,0,0": [[[0, 0, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0]]]}');
const c = JSON.parse('{"-1,0,0,-1": [[[-1, 0, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0]]], "-1,0,0,0": [[[-1, 0, 0, -1], [0, -1, 0, 0], [-1, -1, 0, 0], [-2, 0, 0, 0], [0, -2, 0, 0]], [[0, 0, 0, 0], [0, -1, 0, 0], [-1, -1, 0, 0], [-2, 0, 0, 0], [0, -2, 0, 0]]], "0,-1,0,0": [[[-1, 0, 0, -1], [-1, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0], [-2, 0, 0, 0]], [[0, 0, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0], [-2, 0, 0, 0]]], "-2,0,0,0": [[[-1, 0, 0, -1], [0, -1, 0, 0], [0, -2, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0]], [[0, 0, 0, 0], [0, -1, 0, 0], [0, -2, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0]]], "-1,-1,0,0": [[[-1, 0, 0, -1], [-2, 0, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, -2, 0, 0]], [[0, 0, 0, 0], [-2, 0, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, -2, 0, 0]]], "0,-2,0,0": [[[-1, 0, 0, -1], [-1, -1, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, 0, 0, 0]], [[0, 0, 0, 0], [-1, -1, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, 0, 0, 0]]], "0,0,0,0": [[[-1, 0, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0]]]}');


// Each of the following function gives a number that corresonds
//  to a FoundryVTT "official" result number that matches the result
//  listed
// These were painstakingly copied by hand.
function boost_die_lookup(result) {
    if (array_equals(result, [0, 0, 0, 0])) {
        return 1;
    } else if (array_equals(result, [1, 0, 0, 0])) {
        return 3;
    } else if (array_equals(result, [0, 1, 0, 0])) {
        return 6;
    } else if (array_equals(result, [1, 1, 0, 0])) {
        return 4;
    } else if (array_equals(result, [0, 2, 0, 0])) {
        return 5;
    } else {
        return 7;
    }
}

function ability_die_lookup(result) {
    if (array_equals(result, [0, 0, 0, 0])) {
        return 1;
    } else if (array_equals(result, [1, 0, 0, 0])) {
        return 2;
    } else if (array_equals(result, [0, 1, 0, 0])) {
        return 5;
    } else if (array_equals(result, [2, 0, 0, 0])) {
        return 4;
    } else if (array_equals(result, [1, 1, 0, 0])) {
        return 7;
    } else if (array_equals(result, [0, 2, 0, 0])) {
        return 8;
    } else {
        return 9;
    }
}


function proficiency_die_lookup(result) {
    if (array_equals(result, [0, 0, 0, 0])) {
        return 1;
    } else if (array_equals(result, [1, 0, 0, 0])) {
        return 2;
    } else if (array_equals(result, [0, 1, 0, 0])) {
        return 6;
    } else if (array_equals(result, [2, 0, 0, 0])) {
        return 4;
    } else if (array_equals(result, [1, 1, 0, 0])) {
        return 7;
    } else if (array_equals(result, [0, 2, 0, 0])) {
        return 10;
    } else if (array_equals(result, [1, 0, 1, 0])) {
        return 12;
    } else {
        return 13;
    }
}


function setback_die_lookup(result) {
    if (array_equals(result, [0, 0, 0, 0])) {
        return 1;
    } else if (array_equals(result, [-1, 0, 0, 0])) {
        return 3;
    } else if (array_equals(result, [0, -1, 0, 0])) {
        return 5;
    } else {
        return 7;
    }
}


function difficulty_die_lookup(result) {
    if (array_equals(result, [0, 0, 0, 0])) {
        return 1;
    } else if (array_equals(result, [-1, 0, 0, 0])) {
        return 2;
    } else if (array_equals(result, [0, -1, 0, 0])) {
        return 4;
    } else if (array_equals(result, [-2, 0, 0, 0])) {
        return 3;
    } else if (array_equals(result, [-1, -1, 0, 0])) {
        return 8;
    } else if (array_equals(result, [0, -2, 0, 0])) {
        return 7;
    } else {
        return 9;
    }
}


function challenge_die_lookup(result) {
    if (array_equals(result, [0, 0, 0, 0])) {
        return 1;
    } else if (array_equals(result, [-1, 0, 0, 0])) {
        return 2;
    } else if (array_equals(result, [0, -1, 0, 0])) {
        return 6;
    } else if (array_equals(result, [-2, 0, 0, 0])) {
        return 4;
    } else if (array_equals(result, [-1, -1, 0, 0])) {
        return 8;
    } else if (array_equals(result, [0, -2, 0, 0])) {
        return 10;
    } else if (array_equals(result, [-1, 0, 0, -1])) {
        return 12;
    } else {
        return 13;
    }
}



/*
============================================
============ RAW DATA ENDS HERE ============
============================================
============= TOOK LONG ENOUGH =============
============================================
*/

/*
============================================
======== OBVIOUSLY USEFUL FUNCTIONS ========
============================================
*/
function diff_result(a, b) {
    return a.map((n, i) => n - b[i]);
}

// https://stackoverflow.com/questions/24094466/javascript-sum-two-arrays-in-single-iteration
function sumArrays(...arrays) {
  const n = arrays.reduce((max, xs) => Math.max(max, xs.length), 0);
  const result = Array.from({ length: n });
  return result.map((_, i) => arrays.map(xs => xs[i] || 0).reduce((sum, x) => sum + x, 0));
}

function array_equals(a, b) {
    return a.every((x, i) => x == b[i]);
}
/*
============================================
=========== NOW NORMAL FUNCTIONS ===========
============================================

*/

function get_game_data() {
    // this won't work unless it's on foundry...
    let msg_num = game.messages._source.length - 1;
    while (!game.messages._source[msg_num].hasOwnProperty("roll")){
        msg_num = msg_num - 1;

    }

    const msg_flavor = game.messages._source[msg_num].flavor;
    const dt = JSON.parse(game.messages._source[msg_num].roll);
    const ndp = game.ffg.RollFFG.fromData(dt);

    let dice_and_results = [];
    const original_result = [ndp.ffg.success - ndp.ffg.failure,
                       ndp.ffg.advantage - ndp.ffg.threat,
                       ndp.ffg.triumph,
                       -ndp.ffg.despair]

    ndp.terms.forEach( (element) => {
      if (element.constructor.name != "String") {
        let d_name = element.constructor.name;
        element.results.forEach( (r) => {
          let net_success = r.ffg.success - r.ffg.failure;
          let net_advantage = r.ffg.advantage - r.ffg.threat;
          let triumph = r.ffg.triumph;
          let despair = -r.ffg.despair;
          let r_string = [net_success, net_advantage, triumph, despair].join();
          dice_and_results.push([d_name, r_string]);
        })
      }
    })

    return {
        ndp: ndp,
        msg_flavor: msg_flavor,
        dice_and_results: dice_and_results,
        original_result: original_result,
    };
}


function get_adjacents(dice_face) {
    const d_name = dice_face[0];
    const r_string = dice_face[1];
    let dice_ref = null;
    switch (d_name) {
        case 'BoostDie':
            dice_ref = b;
            break;
        case 'AbilityDie':
            dice_ref = a;
            break;
        case 'ProficiencyDie':
            dice_ref = p;
            break;
        case 'SetbackDie':
            dice_ref = s;
            break;
        case 'DifficultyDie':
            dice_ref = d;
            break;
        case 'ChallengeDie':
            dice_ref = c;
            break;
        default:
    }
    if (dice_ref == null) {
        return [];
    }
    const pos_adj = dice_ref[r_string]
    return pos_adj[Math.floor(Math.random() * pos_adj.length)];
}

function get_all_flips(dice_and_results) {
    let v_flips = {};
    for (var dice_face of dice_and_results) {
        const d_name = dice_face[0];
        if (!v_flips[d_name]) {
            v_flips[d_name] = []
        }
        const r_string = dice_face[1];
        let result = r_string.split(",").map(numStr => parseInt(numStr));
        let adj = get_adjacents(dice_face);
        let flips = [];
        for (var adj_result of adj) {
            let diff = diff_result(adj_result, result);
            if (!diff.every((r) => {
                return r <= 0;
            })) {
                flips.push(diff);
            }
        }
        v_flips[d_name].push(flips);
    }
    return v_flips
}

function filter_and_process_flips(flips) {
    let f_flips = []
    for (var key in flips) {
        const d_name = key;
        let d_flips = flips[key];
        for (var i = 0; i < d_flips.length; i++) {
            const flips = d_flips[i];
            if (flips.length != 0) {
                let d_name_index = d_name + "," + i;
                f_flips.push([d_name_index, flips]);
            }
        }
    }
    return f_flips;
}

function get_fortunes(flips_1, flips_2, flips_3, original_result) {
    let fort = []
    for (var f1 of flips_1[1]) {
        if (flips_2) {
            for (var f2 of flips_2[1]) {
                if (flips_3) {
                    for (var f3 of flips_3[1]) {
                        const data_arr = [sumArrays(original_result, f1, f2, f3),
                                    [flips_1[0], f1],
                                    [flips_2[0], f2],
                                    [flips_3[0], f3]];
                        fort.push(data_arr);
                    }
                } else {
                    const data_arr = [sumArrays(original_result, f1, f2),
                                    [flips_1[0], f1],
                                    [flips_2[0], f2]];
                    fort.push(data_arr);
                }
            }
        } else {
            const data_arr = [sumArrays(original_result, f1),
                                    [flips_1[0], f1]];
            fort.push(data_arr);
        }
    }
    return fort;
}

function get_all_fortunes(flips, original_result) {
    let fortunes = []
    var i, j, k;
    for (i = 0; i < flips.length; i++) {
        for (j = i + 1; j < flips.length; j++) {
            for (k = j + 1; k < flips.length; k++) {
                fortunes = fortunes.concat(get_fortunes(flips[i], flips[j], flips[k], original_result));
            }
        }
    }
    if (fortunes.length == 0) {
        fortunes = fortunes.concat(get_fortunes(flips[0], flips[1], flips[2], original_result));
    }
    return fortunes;
}

function filter_fortunes(fortunes) {
    // filter outcomes
    let f_fortunes = fortunes
    const success_fortunes = f_fortunes.filter((x) => {
        return x[0][0] >= min_successes;
    })
    if (success_fortunes.length) {
        f_fortunes = success_fortunes;
    }

    const no_despair_fortunes = f_fortunes.filter((x) => {
        return -x[0][3] <= max_despairs;
    })
    if (no_despair_fortunes.length) {
        f_fortunes = no_despair_fortunes;
    }
    return f_fortunes;
}

function max_map(str) {
    switch(str) {
        case "Success":
            return 0;
        case "Advantage":
            return 1;
        case "Triumph":
            return 2;
        case "Despair":
            return 3;
        default:
            return 4;
    }
}

function maximize_fortunes(fortunes, max_order) {
    // maximize
    let m_fortunes = fortunes
    for (var m of max_order) {
        let max_val = Math.max(...m_fortunes.map((x) => x[0][m]));
        m_fortunes = m_fortunes.filter((x) => {
            return x[0][m] == max_val;
        });
    }
    return m_fortunes;
}

function find_dice_result_number(d_name, result) {
    switch(d_name) {
        case 'BoostDie':
            return boost_die_lookup(result);
            break;
        case 'AbilityDie':
            return ability_die_lookup(result);
            break;
        case 'ProficiencyDie':
            return proficiency_die_lookup(result);
            break;
        case 'SetbackDie':
            return setback_die_lookup(result);
            break;
        case 'DifficultyDie':
            return difficulty_die_lookup(result);
            break;
        case 'ChallengeDie':
            return challenge_die_lookup(result);
            break;
        default:
            return -1;
    }
}

function update_display(final_fortune, ndp, msg_flavor) {
    // Change each dice -> rewrite result
    for (var i = 1; i < final_fortune.length; i++) {
        let dice = final_fortune[i][0].split(",");
        let diff = final_fortune[i][1];
        const d_name = dice[0];
        const d_num = parseInt(dice[1]);
        for (var j = 0; j < ndp.terms.length; j++) {
            if (d_name == ndp.terms[j].constructor.name) {
                const dice_to_mutate = ndp.terms[j].results[d_num];
                diff[0] += dice_to_mutate.ffg.success;
                diff[0] -= dice_to_mutate.ffg.failure;
                diff[1] += dice_to_mutate.ffg.advantage;
                diff[1] -= dice_to_mutate.ffg.threat;
                diff[2] += dice_to_mutate.ffg.triumph;
                diff[3] -= dice_to_mutate.ffg.despair;

                dice_to_mutate.result = find_dice_result_number(d_name, diff);
            }
        }
    }

    // Change the final result
    if (final_fortune[0][0] >= 0) {
        ndp.ffg.failure = 0;
        ndp.ffg.success = final_fortune[0][0];
    } else {
        ndp.ffg.success = 0
        ndp.ffg.failure = -final_fortune[0][0];
    }
    if (final_fortune[0][1] >= 0) {
        ndp.ffg.threat = 0;
        ndp.ffg.advantage = final_fortune[0][1];
    } else {
        ndp.ffg.advantage = 0;
        ndp.ffg.threat = -final_fortune[0][1];
    }
    ndp.ffg.triumph = final_fortune[0][2];
    ndp.ffg.despair = -final_fortune[0][3];

    ndp.toMessage({speaker: ChatMessage.getSpeaker(),
                   flavor: msg_flavor})
}


function main(maximizers, min_successes, max_despairs) {
    // get the data we'll need from the game - msg_flavor might not be good.
    const {ndp, msg_flavor, dice_and_results, original_result} = get_game_data();
    const flips = get_all_flips(dice_and_results);
    const f_flips = filter_and_process_flips(flips);

    const fortunes = get_all_fortunes(f_flips, original_result);
    const f_fortunes = filter_fortunes(fortunes);

    // get the order to maximize results in
    const max_order = maximizers.map(max_map);
    const m_fortunes = maximize_fortunes(f_fortunes, max_order);
    const final_fortune = m_fortunes[0];

    update_display(final_fortune, ndp, msg_flavor);
}

main(maximizers, min_successes, max_despairs);