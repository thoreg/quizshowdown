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
    @store.createRecord('quiz')

  setupController: (controller, model)->
    controller.set("model", model)
    controller.set('categories', @store.find('category'))
    controller.set('answer1', @store.createRecord('answer'))
    controller.set('answer2', @store.createRecord('answer'))
    controller.set('answer3', @store.createRecord('answer'))
    controller.set('solution', @store.createRecord('answer', {is_solution: true}))

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
          self = this
          @get('model').save().then (quiz) ->
            answer1 = self.get('answer1')
            answer1.set('quiz', quiz)
            answer1.save()

            answer2 = self.get('answer2')
            answer2.set('quiz', quiz)
            answer2.save()

            answer3 = self.get('answer3')
            answer3.set('quiz', quiz)
            answer3.save()

            solution = self.get('solution')
            solution.set('quiz', quiz)
            solution.save()
