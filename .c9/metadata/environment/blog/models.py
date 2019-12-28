{"changed":true,"filter":false,"title":"models.py","tooltip":"/blog/models.py","value":"from django.db import models\nfrom django.utils import timezone\n\nclass Post(models.Model):\n    \n    title = models.CharField(max_length=150)\n    content = models.TextField()\n    created_date = models.DateTimeField(auto_now_add=True)\n    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)\n    views = models.IntegerField(default=0)\n    \n    def __str__(self):\n        return self.title","undoManager":{"mark":2,"position":3,"stack":[[{"start":{"row":11,"column":0},"end":{"row":11,"column":69},"action":"remove","lines":["    image = models.ImageField(upload_to=\"img\", blank=True, null=True)"],"id":5},{"start":{"row":10,"column":64},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"remove","lines":["0"],"id":6},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"remove","lines":["2"]}],[{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["1"],"id":7},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["5"]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":64},"action":"remove","lines":["    tag = models.CharField(max_length=30, blank=True, null=True)"],"id":8},{"start":{"row":9,"column":42},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":9,"column":42},"end":{"row":9,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":127,"mode":"ace/mode/python"}},"timestamp":1577560305229}