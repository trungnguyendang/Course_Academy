# -*- coding: utf-8 -*-

from odoo import models, fields


class Teacher(models.Model):
    _name = 'academy.teacher'
    _description = 'encapsulate teachers information in academy'

    name = fields.Char()
    biography = fields.Html()
    ImageFile = fields.Binary(string="Upload file")

    course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")


class Course(models.Model):
    _inherit = 'product.template'
    _description = 'encapsulate courses information'

    name = fields.Char()

    teacher_id = fields.Many2one('academy.teacher', string="Teacher")
    lesson_id = fields.One2many('academy.lesson', 'course_id', string="Lesson Name")
    lesson = fields.One2many('academy.lesson', 'course_duration', string="Lessons")



class AcademyLesson(models.Model):
    _name = 'academy.lesson'
    _description = 'academy lesson'

    name = fields.Char(string="Lesson")
    description = fields.Text(string="Description")
    duration = fields.Float(string="Lesson duration")
    upload_lessons = fields.Many2many(comodel_name="ir.attachment", string="Upload files")
    reference_link = fields.Char(string="Reference")

    course_duration = fields.Many2one('product.template', string="Duration")
    course_id = fields.Many2one('academy.course', string="Course")


