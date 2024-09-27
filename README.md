# lesson_OB02

Компания разделяет сотрудников на обычных работников и администраторов. 
У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. 
Администраторы, помимо обычных данных пользователей, 
имеют дополнительный уровень доступа и могут добавлять или 
удалять пользователя из системы.

Программа выполняет:

1.Класс User: Этот класс инкапсулирует данные о пользователе: 
ID, имя и уровень доступа ('user' для обычных сотрудников).

2.Класс Admin: Этот класс наследуется от класса User. 
Добавлен дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). 
Класс также содержит методы add_user и remove_user, которые позволяют 
добавлять и удалять пользователей из списка.

3.Инкапсуляция данных: Атрибуты классов защищены от прямого доступа и 
модификации снаружи. Предоставлен доступ к необходимым атрибутам 
через методы (get и set).
 
