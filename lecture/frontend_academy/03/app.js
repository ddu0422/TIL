// let, const 차이
// let은 데이터 변경 가능, const는 데이터 변경 불가 (상수라고 부른다.)

const container = document.getElementById('root');
const ajax = new XMLHttpRequest();
const content = document.createElement('div');
const NEWS_URL = 'https://api.hnpwa.com/v0/news/1.json';
const CONTENT_URL = 'https://api.hnpwa.com/v0/item/@id.json';

function getData(url) {
  ajax.open('GET', url, false);
  ajax.send();

  return JSON.parse(ajax.response);
}

const newsFeed = getData(NEWS_URL);
const ul = document.createElement('ul');

// hash가 변경될 때 발생하는 이벤트
window.addEventListener('hashchange', function () {
  const id = location.hash.substring(1); // hash값을 가져와 #을 제외

  const newsContent = getData(CONTENT_URL.replace('@id', id));
  const title = document.createElement('h1');

  title.innerHTML = newsContent.title;
  content.appendChild(title);
});

for (let i = 0; i < 10; i++) {
  const div = document.createElement('div');

  div.innerHTML = `
    <li>
      <a href="#${newsFeed[i].id}">
        ${newsFeed[i].title} (${newsFeed[i].comments_count})
      </a>
    </li>
  `;

  ul.appendChild(div.firstElementChild);
}

container.appendChild(ul);
container.appendChild(content);
