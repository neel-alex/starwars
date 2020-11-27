flag = true

if (flag) {

msg_num = game.messages._source.length - 1;
while (!game.messages._source[msg_num].hasOwnProperty("roll")){
    msg_num = msg_num - 1;

}

dt = JSON.parse(game.messages._source[msg_num].roll);
ndp = game.ffg.RollFFG.fromData(dt);

dice_and_results = [];
original_result = [ndp.ffg.success - ndp.ffg.failure,
                   ndp.ffg.advantage - ndp.ffg.threat,
                   ndp.ffg.triumph,
                   -ndp.ffg.despair]

ndp.terms.forEach( (element) => {
  if (element.constructor.name != "String") {
    d_name = element.constructor.name;
    element.results.forEach( (r) => {
      // console.log(r);
      net_success = r.ffg.success - r.ffg.failure;
      // console.log(net_success)
      net_advantage = r.ffg.advantage - r.ffg.threat;
      // console.log(net_advantage)
      triumph = r.ffg.triumph;
      despair = -r.ffg.despair;
      r_string = [net_success, net_advantage, triumph, despair].join();
      dice_and_results.push([d_name, r_string]);
    })
  }
})



}


if (!flag) {
    dice_and_results = [["ProficiencyDie","1,0,1,0"],["ProficiencyDie","1,1,0,0"],["AbilityDie","2,0,0,0"],["AbilityDie","0,2,0,0"],["ChallengeDie","-2,0,0,0"],["ChallengeDie","-1,0,0,-1"],["DifficultyDie","0,-1,0,0"],["DifficultyDie","0,0,0,0"],["BoostDie","0,0,0,0"],["BoostDie","1,1,0,0"],["SetbackDie","0,-1,0,0"],["SetbackDie","0,0,0,0"]]
    // can get this in a cleaner way... todo
    original_result = [2, 2, 1, -1];
    sum = [0, 0, 0, 0];
    for (dandr of dice_and_results) {
        nums = dandr[1].split(",").map(numStr => parseInt(numStr));
        sum[0] += nums[0];
        sum[1] += nums[1];
        sum[2] += nums[2];
        sum[3] += nums[3];
    }
}


// output from pretty js adjacency
b = JSON.parse('{"0,0,0,0": [[[0, 1, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]], [[0, 1, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]], "0,1,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0]]], "1,0,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0]]], "1,1,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]], "0,2,0,0": [[[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]]}');
a = JSON.parse('{"2,0,0,0": [[[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]], "1,0,0,0": [[[2, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]], "0,1,0,0": [[[2, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], [[0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]], [[0, 2, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]], "1,1,0,0": [[[2, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]], "0,0,0,0": [[[0, 2, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]], "0,2,0,0": [[[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]]]}');
p = JSON.parse('{"1,0,1,0": [[[1, 0, 0, 0], [2, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]]], "1,0,0,0": [[[1, 0, 1, 0], [2, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]], [[0, 2, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]], "2,0,0,0": [[[1, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0]], [[1, 0, 0, 0], [1, 1, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]], "0,1,0,0": [[[1, 0, 1, 0], [2, 0, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]], "1,1,0,0": [[[1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 2, 0, 0], [2, 0, 0, 0]], [[1, 1, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0]], [[2, 0, 0, 0], [0, 2, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]], "0,2,0,0": [[[1, 0, 1, 0], [1, 1, 0, 0], [2, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]], [[1, 1, 0, 0], [0, 2, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]], "0,0,0,0": [[[1, 0, 0, 0], [0, 2, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [2, 0, 0, 0]]]}');
s = JSON.parse('{"0,0,0,0": [[[-1, 0, 0, 0], [0, -1, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0]], [[-1, 0, 0, 0], [0, -1, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0]]], "-1,0,0,0": [[[0, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0], [0, -1, 0, 0]], [[0, 0, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0], [0, -1, 0, 0]]], "0,-1,0,0": [[[0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0]], [[0, 0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0], [-1, 0, 0, 0]]]}');
d = JSON.parse('{"-2,0,0,0": [[[0, -1, 0, 0], [0, -1, 0, 0], [0, 0, 0, 0]]], "0,-1,0,0": [[[-2, 0, 0, 0], [-1, 0, 0, 0], [0, -2, 0, 0]], [[-2, 0, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0]], [[-1, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0]]], "0,0,0,0": [[[-2, 0, 0, 0], [0, -2, 0, 0], [-1, -1, 0, 0]]], "0,-2,0,0": [[[0, 0, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0]]], "-1,0,0,0": [[[0, -1, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0]]], "-1,-1,0,0": [[[0, 0, 0, 0], [0, -1, 0, 0], [0, -1, 0, 0]]]}');
c = JSON.parse('{"-1,0,0,-1": [[[-1, 0, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0]]], "-1,0,0,0": [[[-1, 0, 0, -1], [0, -1, 0, 0], [-1, -1, 0, 0], [-2, 0, 0, 0], [0, -2, 0, 0]], [[0, 0, 0, 0], [0, -1, 0, 0], [-1, -1, 0, 0], [-2, 0, 0, 0], [0, -2, 0, 0]]], "0,-1,0,0": [[[-1, 0, 0, -1], [-1, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0], [-2, 0, 0, 0]], [[0, 0, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0], [-2, 0, 0, 0]]], "-2,0,0,0": [[[-1, 0, 0, -1], [0, -1, 0, 0], [0, -2, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0]], [[0, 0, 0, 0], [0, -1, 0, 0], [0, -2, 0, 0], [-1, 0, 0, 0], [-1, -1, 0, 0]]], "-1,-1,0,0": [[[-1, 0, 0, -1], [-2, 0, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, -2, 0, 0]], [[0, 0, 0, 0], [-2, 0, 0, 0], [-1, 0, 0, 0], [0, -1, 0, 0], [0, -2, 0, 0]]], "0,-2,0,0": [[[-1, 0, 0, -1], [-1, -1, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, 0, 0, 0]], [[0, 0, 0, 0], [-1, -1, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, 0, 0, 0]]], "0,0,0,0": [[[-1, 0, 0, 0], [0, -1, 0, 0], [-2, 0, 0, 0], [-1, -1, 0, 0], [0, -2, 0, 0]]]}');

// console.log(b);
// console.log(dice_and_results);

// Potential input
maximizers = ["Advantage", "Success", "Triumph", "Despair"];
num_dice = 3;
min_successes = 1;
max_despairs = 0;

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
max_order = maximizers.map(max_map);
// console.log(max_order);


function get_adjacents(dice_face) {
    d_name = dice_face[0];
    r_string = dice_face[1];
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
            dice_ref = null;
    }
    if (dice_ref == null) {
        return [];
    }
    pos_adj = dice_ref[r_string]
    return pos_adj[Math.floor(Math.random() * pos_adj.length)];
}

function diff_result(a, b) {
    return a.map((n, i) => n - b[i]);
}

v_flips = {};
for (dice_face of dice_and_results) {
    d_name = dice_face[0];
    if (!v_flips[d_name]) {
        v_flips[d_name] = []
    }
    r_string = dice_face[1];
    result = r_string.split(",").map(numStr => parseInt(numStr));
    // console.log(result);
    adj = get_adjacents(dice_face);
    flips = [];
    for (adj_result of adj) {
        diff = diff_result(adj_result, result);
        if (!diff.every((r) => {
            return r <= 0;
        })) {
            flips.push(diff);
        }
    }
    v_flips[d_name].push(flips);
}

f_flips = []
for (key in v_flips) {
    d_name = key;
    d_flips = v_flips[key];
    for (i = 0; i < d_flips.length; i++) {
        flips = d_flips[i];
        if (flips.length != 0) {
            d_name_index = d_name + "," + i;
            f_flips.push([d_name_index, flips]);
        }
    }
}

// console.log(f_flips);

// num_dice = Math.min(Object.keys(f_flips).length, num_dice);
// https://stackoverflow.com/questions/24094466/javascript-sum-two-arrays-in-single-iteration
function sumArrays(...arrays) {
  const n = arrays.reduce((max, xs) => Math.max(max, xs.length), 0);
  const result = Array.from({ length: n });
  return result.map((_, i) => arrays.map(xs => xs[i] || 0).reduce((sum, x) => sum + x, 0));
}


function get_fortunes(flips_1, flips_2, flips_3) {
    fort = []
    for (f1 of flips_1[1]) {
        if (flips_2) {
            for (f2 of flips_2[1]) {
                if (flips_3) {
                    for (f3 of flips_3[1]) {
                        data_arr = [sumArrays(original_result, f1, f2, f3),
                                    [flips_1[0], f1],
                                    [flips_2[0], f2],
                                    [flips_3[0], f3]];
                        fort.push(data_arr);
                    }
                } else {
                    data_arr = [sumArrays(original_result, f1, f2),
                                    [flips_1[0], f1],
                                    [flips_2[0], f2]];
                    fort.push(data_arr);
                }
            }
        } else {
            data_arr = [sumArrays(original_result, f1),
                                    [flips_1[0], f1]];
            fort.push(data_arr);
        }
    }
    return fort;
}

n = 0;
fortunes = []
for (i = 0; i < f_flips.length; i++) {
    for (j = i + 1; j < f_flips.length; j++) {
        for (k = j + 1; k < f_flips.length; k++) {
            flips_1 = f_flips[i];
            flips_2 = f_flips[j];
            flips_3 = f_flips[k];
            fortunes = fortunes.concat(get_fortunes(flips_1, flips_2, flips_3));
        }
    }
}

// filter outcomes
success_fortunes = fortunes.filter((x) => {
    return x[0][0] >= min_successes;
})
if (success_fortunes.length) {
    fortunes = success_fortunes;
}

no_despair_fortunes = fortunes.filter((x) => {
    return -x[0][3] <= max_despairs;
})
if (no_despair_fortunes.length) {
    fortunes = no_despair_fortunes;
}

// maximize
for (m of max_order) {
    max_val = Math.max(...fortunes.map((x) => x[0][m]));
    fortunes = fortunes.filter((x) => {
        return x[0][m] == max_val;
    });
}


final_fortune = fortunes[0];

console.log(final_fortune);

function array_equals(a, b) {
    return a.every((x, i) => x == b[i]);
}

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

if (flag) {
    // Change each dice -> rewrite result
    for (i = 1; i < final_fortune.length; i++) {
        dice = final_fortune[i][0].split(",");
        diff = final_fortune[i][1];
        d_name = dice[0];
        d_num = parseInt(dice[1]);
        for (j = 0; j < ndp.terms.length; j++) {
            if (d_name == ndp.terms[j].constructor.name) {
                dice_to_mutate = ndp.terms[j].results[d_num];
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

    ndp.toMessage()
}