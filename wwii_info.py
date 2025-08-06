#!/usr/bin/env python3
"""
World War II Information Application
A simple application that provides information about World War II
"""

import sys
from datetime import datetime


class WWIIInfo:
    """Class containing World War II information and facts"""
    
    def __init__(self):
        self.basic_facts = {
            "duration": "1939-1945",
            "start_date": "September 1, 1939",
            "end_date": "September 2, 1945",
            "total_duration": "6 years and 1 day",
            "casualties": "70-85 million deaths worldwide",
            "major_powers": {
                "Allies": ["United States", "Soviet Union", "United Kingdom", "China", "France"],
                "Axis": ["Germany", "Japan", "Italy"]
            }
        }
        
        self.key_events = [
            {
                "date": "September 1, 1939",
                "event": "Germany invades Poland, marking the beginning of WWII"
            },
            {
                "date": "December 7, 1941",
                "event": "Japan attacks Pearl Harbor, bringing the US into the war"
            },
            {
                "date": "June 6, 1944",
                "event": "D-Day landings in Normandy, France"
            },
            {
                "date": "May 8, 1945",
                "event": "VE Day - Victory in Europe, Germany surrenders"
            },
            {
                "date": "August 6 & 9, 1945",
                "event": "Atomic bombs dropped on Hiroshima and Nagasaki"
            },
            {
                "date": "September 2, 1945",
                "event": "VJ Day - Victory over Japan, Japan formally surrenders"
            }
        ]
        
        self.theaters = {
            "European Theater": {
                "description": "Fighting in Europe, North Africa, and the Atlantic",
                "key_battles": ["Battle of Britain", "Stalingrad", "D-Day", "Battle of the Bulge"]
            },
            "Pacific Theater": {
                "description": "Fighting in the Pacific Ocean, Asia, and the Pacific islands",
                "key_battles": ["Pearl Harbor", "Midway", "Guadalcanal", "Iwo Jima", "Okinawa"]
            }
        }
    
    def display_overview(self):
        """Display a general overview of WWII"""
        print("=" * 60)
        print("WORLD WAR II OVERVIEW")
        print("=" * 60)
        print(f"Duration: {self.basic_facts['duration']}")
        print(f"Start: {self.basic_facts['start_date']}")
        print(f"End: {self.basic_facts['end_date']}")
        print(f"Total Duration: {self.basic_facts['total_duration']}")
        print(f"Estimated Casualties: {self.basic_facts['casualties']}")
        print()
        
        print("MAJOR POWERS:")
        print(f"Allies: {', '.join(self.basic_facts['major_powers']['Allies'])}")
        print(f"Axis: {', '.join(self.basic_facts['major_powers']['Axis'])}")
        print()
    
    def display_key_events(self):
        """Display key events and timeline"""
        print("KEY EVENTS & TIMELINE:")
        print("-" * 40)
        for event in self.key_events:
            print(f"{event['date']}: {event['event']}")
        print()
    
    def display_theaters(self):
        """Display information about the main theaters of war"""
        print("THEATERS OF WAR:")
        print("-" * 40)
        for theater, info in self.theaters.items():
            print(f"\n{theater}:")
            print(f"  {info['description']}")
            print(f"  Key Battles: {', '.join(info['key_battles'])}")
        print()
    
    def display_consequences(self):
        """Display major consequences and aftermath"""
        print("MAJOR CONSEQUENCES & AFTERMATH:")
        print("-" * 40)
        consequences = [
            "Formation of the United Nations (1945)",
            "Beginning of the Cold War between US and Soviet Union",
            "Decolonization movements across Africa and Asia",
            "Establishment of Israel (1948)",
            "Division of Germany and Korea",
            "Nuremberg Trials for war crimes",
            "Major technological advances (radar, jet engines, nuclear technology)",
            "Significant changes in women's roles in society"
        ]
        
        for consequence in consequences:
            print(f"• {consequence}")
        print()
    
    def display_all_info(self):
        """Display all available information about WWII"""
        self.display_overview()
        self.display_key_events()
        self.display_theaters()
        self.display_consequences()


def main():
    """Main function to run the WWII information application"""
    wwii = WWIIInfo()
    
    if len(sys.argv) > 1:
        topic = sys.argv[1].lower()
        if topic == "overview":
            wwii.display_overview()
        elif topic == "events":
            wwii.display_key_events()
        elif topic == "theaters":
            wwii.display_theaters()
        elif topic == "consequences":
            wwii.display_consequences()
        elif topic == "help":
            print("Available topics: overview, events, theaters, consequences")
            print("Usage: python wwii_info.py [topic]")
            print("Or run without arguments to see all information.")
        else:
            print(f"Unknown topic: {topic}")
            print("Available topics: overview, events, theaters, consequences")
            print("Run with 'help' for usage information.")
    else:
        print("World War II Information System")
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        wwii.display_all_info()


if __name__ == "__main__":
    main()
