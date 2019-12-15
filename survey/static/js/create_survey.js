new Vue({
  delimiters: ["[[", "]]"],
  el: "#survey-form",
  data: {
    questionId: 1,
    choiceId: 1,
    questions: []
  },
  methods: {
    addQuestion: function() {
      this.questions.push({
        id: this.questionId,
        text: "",
        choices: [
          {
            id: this.choiceId,
            text: ""
          }
        ]
      });
      this.questionId++;
      this.choiceId++;
    },
    removeQuestion: function(question) {
      var questions = this.questions.slice();
      var idx = questions.indexOf(question);
      questions.splice(idx, 1);
      this.questions = questions;
    },
    addChoice: function(question) {
      question.choices.push({
        id: this.choiceId,
        text: ""
      });
      var idx = this.questions.indexOf(question);
      var questions = this.questions.slice();
      questions[idx] = question;
      this.questions = questions;
      this.choiceId++;
    },
    removeChoice: function(question, choice) {
      var questions = this.questions.slice();
      var qIdx = questions.indexOf(question);
      var cIdx = question.choices.indexOf(choice);
      question.choices.splice(cIdx, 1);
      questions[qIdx] = question;
      this.questions = questions;
    },
    serializeQuestion: function(question) {
      var q = Object.assign({}, question);
      q.choices = q.choices.filter(function(c) {
        return Boolean(c.text);
      });
      return JSON.stringify(q);
    },
    validQuestion: function(question) {
      var valid = Boolean(question.text);
      if (valid) {
        var choices = question.choices.filter(function(c) {
          return Boolean(c.text);
        });
        valid = Boolean(choices);
      }
      return valid;
    }
  },
  mounted: function() {
    this.addQuestion();
  }
});
