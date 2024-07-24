def solution(strings, n):
	strings.sort()
	return sorted(strings, key=lambda x: x[n])


def solution(strings, n):
    answer = []

    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    
    strings.sort()

    for j in range(len(strings)):
        answer.append(strings[j][1:])
        
    return answer




//두 번째와 같은 방법으로 푼 자바스크립트 코드

function solution(strings) {
    let answer = [];

    for (let i = 0; i < strings.length; i++){
        strings[i] = strings[i][n] + strings[i];
    }

    strings.sort();

    for(let j = 0; j < strings.length; j++) {
        strings[j] = strings[j].replace(strings[j][0], "");
        answer.push(strings[j]);
    }

    return answer;
}