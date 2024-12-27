from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import Q

from .models import Group, Album, Song, GroupMember


def home(request):
    groups = Group.objects.all()
    albums = Album.objects.all()
    songs = Song.objects.all()
    members = GroupMember.objects.all()

    return render(request, 'home.html', {
        'groups': groups,
        'albums': albums,
        'songs': songs,
        'members': members,
    })


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    albums = group.albums.all()
    songs = group.songs.all()
    return render(request, 'group_detail.html', {'group': group, 'albums': albums, 'songs': songs})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = album.songs.all()
    return render(request, 'album_detail.html', {'album': album, 'songs': songs})


def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song_detail.html', {'song': song})


def member_detail(request, pk):
    member = get_object_or_404(GroupMember, pk=pk)
    return render(request, 'member_detail.html', {'member': member})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_list.html', {'groups': groups})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums_list.html', {'albums': albums})


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs_list.html', {'songs': songs})


def group_member_list(request):
    members = GroupMember.objects.all()
    return render(request, 'group_members_list.html', {'members': members})


def search_view(request):
    query = request.GET.get("q", "").strip()
    results = {
        "groups": [],
        "albums": [],
        "songs": [],
        "members": [],
    }

    if query:
        results["groups"] = Group.objects.filter(Q(name__icontains=query))
        results["albums"] = Album.objects.filter(Q(name__icontains=query))
        results["songs"] = Song.objects.filter(Q(name__icontains=query))
        results["members"] = GroupMember.objects.filter(Q(name__icontains=query))

    for key, queryset in results.items():
        for obj in queryset:
            obj.url = reverse(f"{key[:-1]}_detail", args=[obj.pk])

    return render(request, "search.html", {"results": results, "query": query})
