<template>
  <div class="chat">
  
    <ul class="list-group">
      <li v-bind:class="{  'list-group': 1, 'bot-chat': line.bot, 'user-chat': !line.bot}" v-for="line in chatlines">{{ line.author }}: {{ line.text }}</li>
    </ul>
    <input v-model="username" placeholder="Jane Doe">
    <input v-model="message" placeholder="Say something">
    <button v-on:click="sendMessage" class="btn btn-outline-primary" >Send</button>
  </div>
</template>

<script>
export default {
  name: 'Chat',
  props: {
    botname: String
  },
  data () {
    return { 
      chatlines: [
        { 
          author: this.botname,
          text: "Hello",
          bot: true
        },
        {
          author: this.botname,
          text: "How are you?",
          bot: true
        }
      ],
      username: '',
      message: ''
    }
  },
  methods: {
    sendMessage: function (event) {
      this.chatlines.push({ "author": this.username, "text": this.message })
      this.message = ''
    }
  }
}
</script>
  
<style scoped>
h1 {
  margin: 40px 0 0;
}
.list-group {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: .75rem 1.25rem;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid rgba(0,0,0,.125);
}
.btn:not(:disabled):not(.disabled) {

    cursor: pointer;

}
[type="reset"], [type="submit"], button, html [type="button"] {

    -webkit-appearance: button;

}
.btn-outline-primary {

    color: #007bff;
    background-color: transparent;
    background-image: none;
    border-color: #007bff;

}
.btn {

    display: inline-block;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    border: 1px solid transparent;
        border-top-color: transparent;
        border-right-color: transparent;
        border-bottom-color: transparent;
        border-left-color: transparent;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: .25rem;
    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;

}
button, select {

    text-transform: none;

}
button, input {

    overflow: visible;

}
button, input, optgroup, select, textarea {

    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;

}
button {

    border-radius: 0;

}
.bot-chat {
  text-align: left
}
.user-chat {
  text-align: right
}
</style>
