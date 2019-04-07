const app = new Vue({
    el: '#app',
    data: {
      botname: 'Diego',
      conversation: [
        'Hi!', 
        'Hello',
      ],
      newInput: '',
      username: 'Anon'
    },
    delimiters: ['[[',']]']
  });