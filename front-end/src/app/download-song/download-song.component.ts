import { Component, OnInit } from '@angular/core';
import { SongService } from '../services/song.service';

@Component({
  selector: 'download-song',
  templateUrl: './download-song.component.html',
  styleUrls: ['./download-song.component.css']
})
export class DownloadSongComponent implements OnInit {

  song_names = []
  constructor(private service: SongService) { }

  ngOnInit() {
  }

  downloadSongs(songs: String){
    this.service.downloadSongs(songs)
  }

}
