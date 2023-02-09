override_class_attr
###################

Purpose
*******

In the Open edX there are lots of places where classes are used as Enum or
dict like objects.

For those classes `@pluggable_override` decorator provides no effect, because
such class objects are never initialized.

The only override option we have on the plugin side for such objects is to
monkeypatch them during the plugin initialization.
