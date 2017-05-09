from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"baseballleagues": League.objects.filter(sport__icontains='baseball'),
		"womenleagues": League.objects.filter(name__icontains='women'),
		"hockeyleagues": League.objects.filter(sport__icontains='hockey'),
		"notfootballs": League.objects.exclude(sport__icontains="football"),
		"atlanticregions": League.objects.filter(name__icontains="atlantic"),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"conferences": League.objects.filter(name__icontains='conference'),
		"places": Team.objects.filter(location__icontains='dallas'),
		"Raptors": Team.objects.filter(team_name__icontains='raptors'),
		"places": Team.objects.filter(location__icontains='city'),
		"teams": Team.objects.filter(team_name__startswith="T"),
		"allteams": Team.objects.order_by("location"),
		"reverses": Team.objects.order_by("-team_name"),
		"lasts": Player.objects.filter(last_name__icontains="cooper"),
		"firsts": Player.objects.filter(first_name__icontains="Joshua"),
		"coopers": Player.objects.filter(last_name__icontains="cooper").exclude(first_name__icontains='Joshua'),
		"alexs": Player.objects.filter(first_name__icontains="alexander")|Player.objects.filter(first_name__icontains="Wyatt"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")