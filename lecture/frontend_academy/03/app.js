// let, const 차이
// let은 데이터 변경 가능, const는 데이터 변경 불가 (상수라고 부른다.)

const ajax = new XMLHttpRequest();
const NEWS_URL = 'https://api.hnpwa.com/v0/news/1.json';

ajax.open('GET', NEWS_URL, false);
ajax.send();

// json형태로 바꿔준다.
const newsFeed = JSON.parse(ajax.response);
const ul = document.createElement('ul');

for (let i = 0; i < 10; i++) {
  const li = document.createElement('li');
  li.innerHTML = newsFeed[i].title;
  ul.appendChild(li);
}

document.getElementById('root').appendChild(ul);
