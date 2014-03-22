App = Em.Application.create
    rootElement: '#ember-application'

App.ApplicationAdapter = DS.DjangoRESTAdapter.extend
  host: 'http://127.0.0.1:8000',
  namespace: 'api'

App.Router.map ->
  @resource "quizzes", ->
    @route "create"

App.QuizzesCreateRoute = Em.Route.extend
  model: ->
    self = this
    quiz = @store.createRecord('quiz')
    quiz.get('answers').then ->
      for _unused in [0..3]
        quiz.get("answers").addObject(self.store.createRecord('answer'))

    return quiz

  setupController: (controller, model)->
    controller.set("model", model)
    controller.set('categories', @store.find('category'))

App.Category = DS.Model.extend
  name: DS.attr('string')

App.Quiz = DS.Model.extend
  question: DS.attr('string')
  category: DS.belongsTo('category')
  answers: DS.hasMany('answer', {async: true})

App.Answer = DS.Model.extend
  text: DS.attr('string')
  quiz: DS.belongsTo('quiz')
  is_solution: DS.attr('boolean')

App.QuizzesCreateController = Em.ObjectController.extend
    actions:
        save: ->
          quiz = @get("model").save()
          debugger
          quiz.get("answers").save()
          # for @get("model.answers")
          #   console.log answers
          # @content.save()

          # createTask: function(taskName) {
          # var person = this.get('model');
          # var task = this.store.createRecord('task', {name: taskName});
          # task.set('person', person);

          # task.save().then(function(task) {
          #   person.get('tasks').pushObject(task);
          # });

          # this.set('newTask', '');

