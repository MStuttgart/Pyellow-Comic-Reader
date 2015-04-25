# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui, QtCore
import main_window_view
import main_window_model


class MainWindowController():
    def __init__(self):
        self.view = main_window_view.MainWindowView(self)
        self.model = main_window_model.MainWindowModel(self)

    def open(self):

        file_path = QtGui.QFileDialog().getOpenFileName(
            self.view, self.view.tr('Open comic file'), '../zzz/quadrinhos',
            self.view.tr(
                'All supported files (*.zip *.cbz *.rar *.cbr *.tar *.cbt);; '
                'Zip Files (*.zip *.cbz);; Rar Files (*.rar *.cbr);; '
                'Tar Files (*.tar *.cbt);; All files (*)'))

        if file_path:
            self.load(file_path)

    def load(self, file_name, initial_page=0):

        self.model = main_window_model.MainWindowModel(self)
        self.view.switch_to_normal_view()

        if self.model.open(file_name, initial_page):
            self.set_view_content(self.model.get_current_page())
            self.view.setWindowTitle(self.model.comic.name +
                                     ' - Pynocchio Comic Reader')
            self.view.enable_actions()
            self.update_statusbar()
        else:
            print '[ERROR] error load comics'

    def save_image(self):
        print

    def online_comics(self):
        self.main_window_view.setCentralWidget(self.web_view)
        print

    def next_page(self):
        self.model.next_page()

    def previous_page(self):
        self.model.previous_page()

    def first_page(self):
        self.model.first_page()

    def last_page(self):
        self.model.last_page()

    def go_to_page(self):
        print

    def next_comic(self):
        print

    def previous_comic(self):
        print

    def rotate_left(self):
        self.model.rotate_left()

    def rotate_right(self):
        self.model.rotate_right()

    def original_fit(self):
        self.model.original_fit()

    def vertical_fit(self):
        self.model.vertical_fit()

    def horizontal_fit(self):
        self.model.horizontal_fit()

    def best_fit(self):
        self.model.best_fit()

    def add_bookmark(self):
        print

    def remove_bookmark(self):
        print

    def bookmark_manager(self):
        print

    def show_toolbar(self):
        print

    def show_statusbar(self):
        print

    def preference_dialog(self):
        print

    def exit(self):
        print 'saindo'

    def show(self):
        self.view.show()

    def set_view_content(self, content):
        self.view.set_viewer_content(content)
        self.update_statusbar()

    def update_current_view_container_size(self, new_size):
        self.model.view_container_size = new_size

    def get_current_view_container_size(self):
        return self.view.get_current_view_container_size()

    def update_statusbar(self):

        if self.model.comic:
            n_page = self.model.comic.get_current_page_number()
            pages_size = self.model.comic.get_number_of_pages()
            page_width = self.model.get_current_page().width()
            page_height = self.model.get_current_page().height()
            page_title = self.model.comic.get_current_page_title()

            self.view.update_status_bar(n_page, pages_size, page_title,
                                        page_width, page_height)
