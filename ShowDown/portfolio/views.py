from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "portfolio/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ############################
        ###### index context #######
        ############################
        context["title"] = "Vivek Chakravorty"  # FIXME: this is hardcoded, change this

        return context


class SkillsView(TemplateView):
    template_name = "portfolio/skills.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ############################
        ###### skills context ######
        ############################
        context["title"] = "Vivek Chakravorty"  # FIXME: this is hardcoded, change this

        return context


class PortfolioView(TemplateView):
    template_name = "portfolio/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ############################
        #### portfolio context #####
        ############################
        context["title"] = "Vivek Chakravorty"  # FIXME: this is hardcoded, change this

        return context


class ProjectsView(TemplateView):
    template_name = "portfolio/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ############################
        ##### projects context #####
        ############################
        context["title"] = "Vivek Chakravorty"  # FIXME: this is hardcoded, change this

        return context


class ContactView(TemplateView):
    template_name = "portfolio/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ############################
        ##### contact context ######
        ############################
        context["title"] = "Vivek Chakravorty"  # FIXME: this is hardcoded, change this

        return context
