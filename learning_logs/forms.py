from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """用户创建主题的表单"""
    class Meta:
        model = Topic # 根据topic创建表单
        fields = ['text']  # 表单包含text字段
        labels = {'text': ''}  # 不要为text生成标签

class EntryForm(forms.ModelForm):
    """用户创建内容的表单"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # 使用80列的输入框
