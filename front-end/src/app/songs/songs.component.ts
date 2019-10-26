import { Song } from './../models/song';
import { SongService } from './../services/song.service';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'songs',
  templateUrl: './songs.component.html',
  styleUrls: ['./songs.component.css']
})
export class SongsComponent implements OnInit {
  
  songs: Song[];

  constructor(private service: SongService) { }

  ngOnInit() {
    this.getSongs();
  }

  getSongs(){
    this.service.getSongs().subscribe((data: any) => {
      this.songs = data.data;
    });
  }

}
