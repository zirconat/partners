# original card code
            # st.markdown(
            #     f"""
            #     <div style="border-radius: 10px; border: 1px solid #ccc; padding: 10px; margin-bottom: 20px; background-color: #f9f9f9;">
            #         <div style="float: right; background-color: {get_status_color(employee_data['Status'])}; color: white; padding: 5px 10px; border-radius: 5px;">
            #             {employee_data['Status']}
            #         </div>
            #         <div style="float: right; color: white; padding: 5px 10px; border-radius: 5px;">
            #         </div>
            #         <div style="float: right; background-color: {get_tier_color(employee_data['Tier'])}; color: white; padding: 5px 10px; border-radius: 5px;">
            #             <b>Tier: </b>{employee_data['Tier']}
            #         </div>
            #         <p style="font-weight: bold; font-size: 25px; color: black;">
            #             {employee_data['Name']} ({employee_data['Designation']}), {employee_data['Company']}    
            #         </p>                  
            #         <div style="display: flex; flex-wrap: wrap;">
            #             <div style="flex: 1; margin-right: 10px;">
            #                 <p style="color: black;"><b>Country:</b><br>{employee_data['Country']}</p>
            #                 <p style="color: black;"><b>Contact No.:</b><br> {int(employee_data['Contact No.'])}</p>
            #                 <p style="color: black;"><b>Vehicle(s):</b><br> {employee_data['Vehicle']}</p>
            #                 <p style="color: black;"><b>Address:</b><br> {employee_data['Address']}</p>
            #             </div>
            #             <div style="flex: 1; margin-right: 10px;">
            #                 <p style="color: black;"><b>Posting Date:</b><br> {formatted_posting_date}</p>
            #                 <p style="color: black;"><b>De-posted Date:</b><br> {formatted_deposted_date}</p>
            #                 <p style="color: black;"><b>Golf:</b><br> {employee_data['Golf']}</p>
            #                 <p style="color: black;"><b>Golf Handicap:</b><br> {employee_data['Golf Handicap']}</p>
            #             </div>
            #             <div style="flex: 1; margin-right: 10px;">
            #                 <p style="color: black;"><b>Dietary Restrictions:</b><br> {employee_data['Dietary Restrictions']}</p>
            #                 <p style="color: black;"><b>Reception:</b><br> {employee_data['Reception']}</p>
            #                 <p style="color: black;"><b>Festivity:</b><br> {employee_data['Festivity']}</p>
            #             </div>
            #             <div style="flex: 1; margin-right: 10px;">
            #                 <p style="color: black;"><b>BigS/SmallS:</b><br> {employee_data['BigS/SmallS']}</p>
            #                 <p style="color: black;"><b>Interest(s):</b><br> {employee_data['Interests']} </p>
            #             </div>
            #         </div>
            #     </div>
            #     """,
            #     unsafe_allow_html=True
            # )