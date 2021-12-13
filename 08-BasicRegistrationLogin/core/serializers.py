from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'name', 'desc']
  
  def create(self, validated_data):
    author = Author(
      name=validated_data['name'],
      desc=validated_data['desc']
    )
    author.save()
    return author


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id', 'title', 'writers', 'created', 'updated']
    depth = 1


  def validate(self, data):
    method = self.context['request'].method
    # create | update
    if method == ("POST" or "PUT"):
      writers = self.initial_data.get('writers', [])
      try:
        for writer in writers:
          auth = Author.objects.get(pk=writer)
      except Exception as err:
        error = {"writers": [f"Author not found by id: {writer}"]}
        raise serializers.ValidationError(error)
    return data
  

  def create(self, validated_data):
    book = Book(**validated_data)
    book.save()

    writers = self.initial_data.get('writers', [])
    if type(writers) == list:
      try:
        book.writers.set(writers)
      except Exception as err:
        pass
    return book
  

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.save()

    writers = self.initial_data.get('writers', [])
    if type(writers) == list:
      try:
        instance.writers.set(writers)
      except Exception as err:
        pass
    
    return instance
