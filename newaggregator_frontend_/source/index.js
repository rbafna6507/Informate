import React from 'react';
import ReactDOM from 'react-dom';
// import './style.css';

// function createNode(element) {
//     return document.createElement(element);
// }

// function append(parent, el) {
//   return parent.appendChild(el);
// }

// // Send the same request
// fetch('https://newsaggregator-api.herokuapp.com/')
//     .then(function (response) {
//         return response.json(); // But parse it as JSON this time
//     })
//     .then(function (json) {
//         console.log('GET response as JSON:');
//         console.log(json);
//         lets_do_it("nytimes", json);
//         lets_do_it("reuters", json);
//         lets_do_it("wired", json);
//         lets_do_it("economist", json);
//         lets_do_it("bbc", json);
//         $(function () {
//             $('[data-toggle="popover"]').popover()
// })
// })
// function lets_do_it(ul_id, resp){
//     const ul = document.getElementById(ul_id)
//     for(var i = 0; i <= 5; i++){
//         let document = JSON.stringify(resp[0]);
//         document = JSON.parse(document);
//         headline = document[0];
//         summary = document[1];
//         link = document[2];
//         source = document[3];
//         // document.getElementById("bruhh").innerHTML = headline
//         let li = createNode('li'), a = createNode('a');
//         a.href = link;
//         a.innerHTML = headline;
//         a.target = "_blank";
//         a.dataset.toggle = "popover";
//         a.dataset.placement = "right";
//         a.dataset.content = summary;
//         a.dataset.trigger = "hover";
//         a.title = source;
//         append(li, a);
//         append(ul, li);
//         resp.shift();
//     }
// }