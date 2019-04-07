const Chatline = Vue.component('chatline', {
    props: ['message', 'author'],
    template: '<div><h3>{{ author }}</h3><p>{{ message }}</p></div>'
   });