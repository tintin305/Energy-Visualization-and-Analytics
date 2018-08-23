// // Generated by CoffeeScript 1.6.3
// /*
// Source, bug reports, examples: https://github.com/tamc/Sankey
// Copyright: Thomas Counsell 2010, 2011
// Licence: MIT Open Source licence http://www.opensource.org/licenses/mit-license.php
// */


// (function() {
//   var FlowLine, Sankey, TransformationBox,
//     __hasProp = {}.hasOwnProperty,
//     __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

//   Sankey = (function() {
//     function Sankey() {
//       this.display_in_element = 'sankey';
//       this.display_width = $("#" + this.display_in_element).width();
//       this.display_height = $("#" + this.display_in_element).height();
//       this.r = Raphael(this.display_in_element, this.display_width, this.display_height);
//       this.left_margin = 100;
//       this.right_margin = 100;
//       this.y_space = 10;
//       this.threshold_for_drawing = 0;
//       this.box_width = 50;
//       this.flow_edge_width = 2;
//       this.flow_curve = 0.25;
//       this.boxes = {};
//       this.box_array = [];
//       this.lines = {};
//       this.line_array = [];
//       this.stacks = [];
//       this.bubbles = [];
//       this.bubbleColor = '#000';
//       this.bubbleLabelColor = '#fff';
//       this.opacity = '1.0';
//       this.opacity_highlight = '0.1';
//     }

//     Sankey.prototype.find_or_create_transformation_box = function(name) {
//       var new_box;
//       if (this.boxes[name] == null) {
//         new_box = new TransformationBox(this, name);
//         this.boxes[name] = new_box;
//         this.box_array.push(new_box);
//       }
//       return this.boxes[name];
//     };

//     Sankey.prototype.lineName = function(start, end) {
//       return "" + start + "-" + end;
//     };

//     Sankey.prototype.createLine = function(datum) {
//       var new_line;
//       if (datum[0] === 0) {
//         return;
//       }
//       new_line = new FlowLine(this, datum[0], datum[1], datum[2]);
//       this.lines[this.lineName(datum[0], datum[2])] = new_line;
//       return this.line_array.push(new_line);
//     };

//     Sankey.prototype.setData = function(data) {
//       var datum, _i, _len, _results;
//       _results = [];
//       for (_i = 0, _len = data.length; _i < _len; _i++) {
//         datum = data[_i];
//         _results.push(this.createLine(datum));
//       }
//       return _results;
//     };

//     Sankey.prototype.setBubbles = function(data) {
//       return this.bubbles = data;
//     };

//     Sankey.prototype.updateData = function(data) {
//       var datum, line, _i, _len, _results;
//       _results = [];
//       for (_i = 0, _len = data.length; _i < _len; _i++) {
//         datum = data[_i];
//         line = this.lines[this.lineName(datum[0], datum[2])];
//         if (line) {
//           _results.push(line.setFlow(datum[1]));
//         } else {
//           _results.push(this.createLine(datum));
//         }
//       }
//       return _results;
//     };

//     Sankey.prototype.convert_flow_values_callback = function(flow) {
//       return flow;
//     };

//     Sankey.prototype.convert_flow_labels_callback = function(flow) {
//       return flow;
//     };

//     Sankey.prototype.convert_box_value_labels_callback = function(flow) {
//       return this.convert_flow_labels_callback(flow);
//     };

//     Sankey.prototype.convert_box_description_labels_callback = function(name) {
//       return name;
//     };

//     Sankey.prototype.convert_bubble_values_callback = function(size) {
//       return size;
//     };

//     Sankey.prototype.convert_bubble_labels_callback = function(size) {
//       return size;
//     };

//     Sankey.prototype.nudge_boxes_callback = function() {
//       return void 0;
//     };

//     Sankey.prototype.nudge_colours_callback = function() {
//       return void 0;
//     };

//     Sankey.prototype.stack = function(x, box_names, y_box) {
//       return this.stacks.push({
//         x: x,
//         box_names: box_names,
//         y_box: y_box
//       });
//     };

//     Sankey.prototype.setColors = function(colors) {
//       var box, box_name, color, _results;
//       _results = [];
//       for (box_name in colors) {
//         if (!__hasProp.call(colors, box_name)) continue;
//         color = colors[box_name];
//         box = this.find_or_create_transformation_box(box_name);
//         _results.push(box.line_colour = colors[box.name] || box.line_colour);
//       }
//       return _results;
//     };

//     Sankey.prototype.recolour = function(lines, new_colour) {
//       var line, _i, _len, _results;
//       _results = [];
//       for (_i = 0, _len = lines.length; _i < _len; _i++) {
//         line = lines[_i];
//         _results.push(line.colour = new_colour);
//       }
//       return _results;
//     };

//     Sankey.prototype.calculateXStep = function() {
//       var maximum_x, stack, _i, _len, _ref;
//       maximum_x = 0;
//       _ref = this.stacks;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         stack = _ref[_i];
//         if (stack.x > maximum_x) {
//           maximum_x = stack.x;
//         }
//       }
//       return (this.display_width - this.left_margin - this.right_margin) / maximum_x;
//     };

//     Sankey.prototype.position_boxes_and_lines = function() {
//       var box, bubble, name, stack, x, x_step, y, _i, _j, _k, _l, _len, _len1, _len2, _len3, _ref, _ref1, _ref2, _ref3, _ref4, _ref5;
//       x_step = this.calculateXStep();
//       _ref = this.stacks;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         stack = _ref[_i];
//         x = stack.x;
//         if (stack.y_box != null) {
//           y = ((_ref1 = this.boxes[stack.y_box]) != null ? _ref1.y : void 0) || 10;
//         } else {
//           y = 10;
//         }
//         _ref2 = stack.box_names;
//         for (_j = 0, _len1 = _ref2.length; _j < _len1; _j++) {
//           name = _ref2[_j];
//           box = this.boxes[name];
//           if (box == null) {

//           } else {
//             box.y = y;
//             box.x = this.left_margin + (x * x_step);
//             y = box.b() + this.y_space;
//           }
//         }
//       }
//       this.nudge_boxes_callback();
//       _ref3 = this.box_array;
//       for (_k = 0, _len2 = _ref3.length; _k < _len2; _k++) {
//         box = _ref3[_k];
//         box.position_and_colour_lines();
//       }
//       _ref4 = this.bubbles;
//       for (_l = 0, _len3 = _ref4.length; _l < _len3; _l++) {
//         bubble = _ref4[_l];
//         if ((_ref5 = this.boxes[bubble[0]]) != null) {
//           _ref5.bubbleValue = bubble[1];
//         }
//       }
//       this.nudge_colours_callback();
//       return this.line_array.sort(function(a, b) {
//         return b.size - a.size;
//       });
//     };

//     Sankey.prototype.draw = function() {
//       var box, line, _i, _j, _len, _len1, _ref, _ref1, _results;
//       this.position_boxes_and_lines();
//       _ref = this.line_array;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         line = _ref[_i];
//         if (line.size > this.threshold_for_drawing) {
//           line.draw(this.r);
//         }
//       }
//       _ref1 = this.box_array;
//       _results = [];
//       for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
//         box = _ref1[_j];
//         if (box.size() > this.threshold_for_drawing) {
//           _results.push(box.draw(this.r));
//         } else {
//           _results.push(void 0);
//         }
//       }
//       return _results;
//     };

//     Sankey.prototype.redraw = function() {
//       var box, line, _i, _j, _len, _len1, _ref, _ref1, _results;
//       this.position_boxes_and_lines();
//       _ref = this.line_array;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         line = _ref[_i];
//         line.redraw(this.r);
//       }
//       _ref1 = this.box_array;
//       _results = [];
//       for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
//         box = _ref1[_j];
//         _results.push(box.redraw(this.r));
//       }
//       return _results;
//     };

//     Sankey.prototype.fade_unless_highlighted = function() {
//       var box, line, _i, _j, _len, _len1, _ref, _ref1, _results;
//       _ref = this.line_array;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         line = _ref[_i];
//         line.fade_unless_highlighted();
//         void 0;
//       }
//       _ref1 = this.box_array;
//       _results = [];
//       for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
//         box = _ref1[_j];
//         box.fade_unless_highlighted();
//         _results.push(void 0);
//       }
//       return _results;
//     };

//     Sankey.prototype.un_fade = function() {
//       var box, line, _i, _j, _len, _len1, _ref, _ref1, _results;
//       _ref = this.line_array;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         line = _ref[_i];
//         line.un_fade();
//         void 0;
//       }
//       _ref1 = this.box_array;
//       _results = [];
//       for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
//         box = _ref1[_j];
//         box.un_fade();
//         _results.push(void 0);
//       }
//       return _results;
//     };

//     return Sankey;

//   })();

//   FlowLine = (function() {
//     function FlowLine(sankey, left_box_name, flow, right_box_name) {
//       this.sankey = sankey;
//       this.hover_stop = __bind(this.hover_stop, this);
//       this.hover_start = __bind(this.hover_start, this);
//       this.setFlow(flow);
//       this.colour = void 0;
//       this.ox = 0;
//       this.oy = 0;
//       this.dx = 0;
//       this.dy = 0;
//       this.left_box = this.sankey.find_or_create_transformation_box(left_box_name);
//       this.right_box = this.sankey.find_or_create_transformation_box(right_box_name);
//       this.left_box.right_lines.push(this);
//       this.right_box.left_lines.push(this);
//     }

//     FlowLine.prototype.setFlow = function(flow) {
//       this.flow = flow;
//       return this.size = this.sankey.convert_flow_values_callback(this.flow);
//     };

//     FlowLine.prototype.labelText = function() {
//       return this.sankey.convert_flow_labels_callback(this.flow);
//     };

//     FlowLine.prototype.path = function() {
//       var curve;
//       curve = (this.dx - this.ox) * this.sankey.flow_curve;
//       return "M " + this.ox + "," + this.oy + " Q " + (this.ox + curve) + "," + this.oy + " " + ((this.ox + this.dx) / 2) + "," + ((this.oy + this.dy) / 2) + " Q " + (this.dx - curve) + "," + this.dy + " " + this.dx + "," + this.dy;
//     };

//     FlowLine.prototype.innerWidth = function() {
//       if (this.size > this.sankey.flow_edge_width) {
//         return this.size - this.sankey.flow_edge_width;
//       }
//       return this.size;
//     };

//     FlowLine.prototype.innerColor = function() {
//       var c;
//       c = Raphael.rgb2hsb(this.colour);
//       if (c.h !== 0 && c.s !== 0) {
//         if (c.b > 0.5) {
//           c.b = c.b - 0.15;
//         } else {
//           c.b = c.b + 0.15;
//         }
//       }
//       return Raphael.hsb2rgb(c.h, c.s, c.b);
//     };

//     FlowLine.prototype.draw = function(r) {
//       this.outer_line = r.path(this.path()).attr({
//         'stroke-width': this.size,
//         'stroke': this.colour
//       });
//       this.inner_line = r.path(this.path()).attr({
//         'stroke-width': this.innerWidth(),
//         'stroke': this.innerColor()
//       });
//       r.set().push(this.inner_line, this.outer_line).hover(this.hover_start, this.hover_stop);
//       this.left_label = r.text(this.ox + 1, this.oy - (this.size / 2) - 5, this.labelText()).attr({
//         'text-anchor': 'start'
//       });
//       this.right_label = r.text(this.dx - 1, this.dy - (this.size / 2) - 5, this.labelText()).attr({
//         'text-anchor': 'end'
//       });
//       this.left_label.hide();
//       return this.right_label.hide();
//     };

//     FlowLine.prototype.hover_start = function(event) {
//       this.highlight(true, true);
//       return this.sankey.fade_unless_highlighted();
//     };

//     FlowLine.prototype.hover_stop = function(event) {
//       this.un_highlight(true, true);
//       return this.sankey.un_fade();
//     };

//     FlowLine.prototype.redraw = function(r) {
//       if (this.outer_line == null) {
//         this.draw(r);
//       }
//       this.outer_line.attr({
//         path: this.path(),
//         'stroke-width': this.size
//       });
//       this.inner_line.attr({
//         path: this.path(),
//         'stroke-width': this.innerWidth()
//       });
//       this.left_label.attr({
//         text: this.labelText(),
//         x: this.ox + 1,
//         y: this.oy - (this.size / 2) - 5
//       });
//       return this.right_label.attr({
//         text: this.labelText(),
//         x: this.dx - 1,
//         y: this.dy - (this.size / 2) - 5
//       });
//     };

//     FlowLine.prototype.fade_unless_highlighted = function() {
//       if (this.outer_line == null) {
//         return false;
//       }
//       if (this.inner_line == null) {
//         return false;
//       }
//       if (this.highlighed === true) {
//         return false;
//       }
//       this.outer_line.attr({
//         'opacity': this.sankey.opacity_highlight
//       });
//       return this.inner_line.attr({
//         'opacity': this.sankey.opacity_highlight
//       });
//     };

//     FlowLine.prototype.un_fade = function() {
//       if (this.outer_line == null) {
//         return false;
//       }
//       if (this.inner_line == null) {
//         return false;
//       }
//       if (this.highlighed === true) {
//         return false;
//       }
//       this.outer_line.attr({
//         'opacity': this.sankey.opacity
//       });
//       return this.inner_line.attr({
//         'opacity': this.sankey.opacity
//       });
//     };

//     FlowLine.prototype.highlight = function(left, right) {
//       if (this.outer_line == null) {
//         return false;
//       }
//       if (this.inner_line == null) {
//         return false;
//       }
//       this.highlighed = true;
//       if (left) {
//         this.left_label.toFront();
//         this.left_label.show();
//         this.left_box.highlight();
//       }
//       if (right) {
//         this.right_label.toFront();
//         this.right_label.show();
//         return this.right_box.highlight();
//       }
//     };

//     FlowLine.prototype.un_highlight = function(left, right) {
//       if (this.outer_line == null) {
//         return false;
//       }
//       this.highlighed = false;
//       if (left) {
//         this.left_label.hide();
//         this.left_box.un_highlight();
//       }
//       if (right) {
//         this.right_label.hide();
//         return this.right_box.un_highlight();
//       }
//     };

//     return FlowLine;

//   })();

//   TransformationBox = (function() {
//     function TransformationBox(sankey, name) {
//       this.sankey = sankey;
//       this.name = name;
//       this.hover_end = __bind(this.hover_end, this);
//       this.hover_start = __bind(this.hover_start, this);
//       this.label_text = this.sankey.convert_box_description_labels_callback(name);
//       this.line_colour = "orange";
//       this.left_lines = [];
//       this.right_lines = [];
//       this.x = 0;
//       this.y = 0;
//       this.bubbleValue = null;
//     }

//     TransformationBox.prototype.b = function() {
//       return this.y + this.size();
//     };

//     TransformationBox.prototype.is_left_box = function() {
//       return this.left_lines.length === 0;
//     };

//     TransformationBox.prototype.is_right_box = function() {
//       return this.right_lines.length === 0;
//     };

//     TransformationBox.prototype.size = function() {
//       var line, lines, s, _i, _len;
//       s = 0;
//       if (this.is_left_box()) {
//         lines = this.right_lines;
//       } else {
//         lines = this.left_lines;
//       }
//       for (_i = 0, _len = lines.length; _i < _len; _i++) {
//         line = lines[_i];
//         if (line.size > this.sankey.threshold_for_drawing) {
//           s = s + line.size;
//         }
//       }
//       return s;
//     };

//     TransformationBox.prototype.flow = function() {
//       var line, lines, s, _i, _len;
//       s = 0;
//       if (this.is_left_box()) {
//         lines = this.right_lines;
//       } else {
//         lines = this.left_lines;
//       }
//       for (_i = 0, _len = lines.length; _i < _len; _i++) {
//         line = lines[_i];
//         if (line.size > this.sankey.threshold_for_drawing) {
//           s = s + line.flow;
//         }
//       }
//       return s;
//     };

//     TransformationBox.prototype.position_and_colour_lines = function() {
//       var box_width, left_lines, line, ly, right_lines, ry, _i, _j, _len, _len1, _results;
//       ly = this.y;
//       left_lines = this.left_lines;
//       left_lines.sort(function(a, b) {
//         return a.left_box.y - b.left_box.y;
//       });
//       for (_i = 0, _len = left_lines.length; _i < _len; _i++) {
//         line = left_lines[_i];
//         line.dx = this.x;
//         line.dy = ly + (line.size / 2);
//         ly = ly + line.size;
//       }
//       ry = this.y;
//       right_lines = this.right_lines;
//       right_lines.sort(function(a, b) {
//         return a.right_box.y - b.right_box.y;
//       });
//       box_width = this.sankey.box_width;
//       _results = [];
//       for (_j = 0, _len1 = right_lines.length; _j < _len1; _j++) {
//         line = right_lines[_j];
//         if (line.colour == null) {
//           line.colour = this.line_colour;
//         }
//         line.ox = this.x + box_width;
//         line.oy = ry + (line.size / 2);
//         _results.push(ry = ry + line.size);
//       }
//       return _results;
//     };

//     TransformationBox.prototype.valueLabelText = function() {
//       return this.sankey.convert_box_value_labels_callback(this.flow());
//     };

//     TransformationBox.prototype.descriptionLabelText = function() {
//       return this.label_text;
//     };

//     TransformationBox.prototype.labelPositionX = function() {
//       if (this.is_left_box()) {
//         return this.x - 3.0;
//       }
//       if (this.is_right_box()) {
//         return this.x + this.sankey.box_width + 3.0;
//       }
//       return this.x + (this.sankey.box_width / 2);
//     };

//     TransformationBox.prototype.labelPositionY = function() {
//       return this.y + (this.size() / 2);
//     };

//     TransformationBox.prototype.labelAttributes = function() {
//       if (this.is_left_box()) {
//         return {
//           'text-anchor': 'end'
//         };
//       }
//       if (this.is_right_box()) {
//         return {
//           'text-anchor': 'start'
//         };
//       }
//       return {};
//     };

//     TransformationBox.prototype.numberLabelPositionX = function() {
//       return this.x + (this.sankey.box_width / 2);
//     };

//     TransformationBox.prototype.numberLabelPositionY = function() {
//       return this.y - 5;
//     };

//     TransformationBox.prototype.bubbleSize = function() {
//       return Math.sqrt(this.sankey.convert_bubble_values_callback(Math.abs(this.bubbleValue)));
//     };

//     TransformationBox.prototype.bubbleLabel = function() {
//       return this.sankey.convert_bubble_labels_callback(this.bubbleValue);
//     };

//     TransformationBox.prototype.bubbleColourForValue = function() {
//       if (this.bubbleValue > 0) {
//         return this.sankey.bubbleColor;
//       }
//       if (this.sankey.negativeBubbleColor == null) {
//         return this.sankey.bubbleColor;
//       }
//       return this.sankey.negativeBubbleColor;
//     };

//     TransformationBox.prototype.bubbleLabelColourForValue = function() {
//       if (this.bubbleValue > 0) {
//         return this.sankey.bubbleLabelColor;
//       }
//       if (this.sankey.negativeBubbleLabelColor == null) {
//         return this.sankey.bubbleLabelColor;
//       }
//       return this.sankey.negativeBubbleLabelColor;
//     };

//     TransformationBox.prototype.draw = function(r) {
//       var box_width;
//       if (!(this.size() > this.sankey.threshold_for_drawing)) {
//         return false;
//       }
//       box_width = this.sankey.box_width;
//       this.box = r.rect(this.x, this.y, box_width, this.size()).attr({
//         'fill': "#E8E2FF",
//         "stroke": "#D4CBF2"
//       });
//       this.label = r.text(this.labelPositionX(), this.labelPositionY(), this.descriptionLabelText()).attr(this.labelAttributes());
//       if (this.bubbleValue != null) {
//         this.bubble_circle = r.circle(this.x + box_width, this.y, this.bubbleSize()).attr({
//           'fill': this.bubbleColourForValue(),
//           'stroke-width': 0
//         });
//         this.bubble_label = r.text(this.x + box_width, this.y, this.bubbleLabel()).attr({
//           'stroke': this.bubbleLabelColourForValue(),
//           'text-anchor': 'middle'
//         });
//       }
//       this.number_label = r.text(this.numberLabelPositionX(), this.numberLabelPositionY(), this.valueLabelText());
//       this.number_label.hide();
//       return r.set().push(this.number_label, this.label, this.box, this.bubble_circle, this.bubble_label).hover(this.hover_start, this.hover_end);
//     };

//     TransformationBox.prototype.redraw = function(r) {
//       if (this.box == null) {
//         this.draw(r);
//       }
//       if (this.box == null) {
//         return;
//       }
//       this.box.attr({
//         y: this.y,
//         height: this.size()
//       });
//       this.label.attr({
//         y: this.labelPositionY()
//       });
//       this.number_label.attr({
//         y: this.numberLabelPositionY(),
//         text: this.valueLabelText()
//       });
//       if (this.bubbleValue != null) {
//         if (this.bubble_circle != null) {
//           this.bubble_circle.attr({
//             cy: this.y,
//             r: this.bubbleSize(),
//             fill: this.bubbleColourForValue()
//           });
//           this.bubble_label.attr({
//             y: this.y,
//             text: this.bubbleLabel(),
//             'stroke': this.bubbleLabelColourForValue()
//           });
//         } else {
//           this.draw(r);
//         }
//       }
//       if (this.size() <= this.sankey.threshold_for_drawing) {
//         this.box.hide();
//         this.label.hide();
//         if (this.bubble_circle != null) {
//           return this.bubble_circle.hide();
//         }
//       } else {
//         this.box.show();
//         this.label.show();
//         if (this.bubble_circle != null) {
//           return this.bubble_circle.show();
//         }
//       }
//     };

//     TransformationBox.prototype.hover_start = function() {
//       var line, _i, _j, _len, _len1, _ref, _ref1;
//       this.highlight();
//       this.number_label.toFront();
//       this.number_label.show();
//       _ref = this.left_lines;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         line = _ref[_i];
//         line.highlight(true, false);
//       }
//       _ref1 = this.right_lines;
//       for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
//         line = _ref1[_j];
//         line.highlight(false, true);
//       }
//       return this.sankey.fade_unless_highlighted();
//     };

//     TransformationBox.prototype.hover_end = function() {
//       var line, _i, _j, _len, _len1, _ref, _ref1;
//       this.un_highlight();
//       this.number_label.hide();
//       _ref = this.left_lines;
//       for (_i = 0, _len = _ref.length; _i < _len; _i++) {
//         line = _ref[_i];
//         line.un_highlight(true, false);
//       }
//       _ref1 = this.right_lines;
//       for (_j = 0, _len1 = _ref1.length; _j < _len1; _j++) {
//         line = _ref1[_j];
//         line.un_highlight(false, true);
//       }
//       return this.sankey.un_fade();
//     };

//     TransformationBox.prototype.highlight = function() {
//       if (this.box == null) {
//         return false;
//       }
//       return this.highlighed = true;
//     };

//     TransformationBox.prototype.un_highlight = function() {
//       if (this.box == null) {
//         return false;
//       }
//       return this.highlighed = false;
//     };

//     TransformationBox.prototype.fade_unless_highlighted = function() {
//       if (this.box == null) {
//         return false;
//       }
//       if (this.highlighed === true) {
//         return false;
//       }
//       this.box.attr({
//         'opacity': this.sankey.opacity_highlight
//       });
//       this.label.attr({
//         'opacity': this.sankey.opacity_highlight
//       });
//       if (this.bubble_circle != null) {
//         this.bubble_circle.attr({
//           'opacity': this.sankey.opacity_highlight
//         });
//       }
//       if (this.bubble_label != null) {
//         return this.bubble_label.attr({
//           'opacity': this.sankey.opacity_highlight
//         });
//       }
//     };

//     TransformationBox.prototype.un_fade = function() {
//       if (this.box == null) {
//         return false;
//       }
//       if (this.highlighed === true) {
//         return false;
//       }
//       this.box.attr({
//         'opacity': this.sankey.opacity
//       });
//       this.label.attr({
//         'opacity': this.sankey.opacity
//       });
//       if (this.bubble_circle != null) {
//         this.bubble_circle.attr({
//           'opacity': this.sankey.opacity
//         });
//       }
//       if (this.bubble_label != null) {
//         return this.bubble_label.attr({
//           'opacity': this.sankey.opacity
//         });
//       }
//     };

//     return TransformationBox;

//   })();

//   window.Sankey = Sankey;

// }).call(this);
d3.sankey = function() {
  var sankey = {},
      nodeWidth = 24,
      nodePadding = 8,
      size = [1, 1],
      nodes = [],
      links = [];
 
  sankey.nodeWidth = function(_) {
    if (!arguments.length) return nodeWidth;
    nodeWidth = +_;
    return sankey;
  };
 
  sankey.nodePadding = function(_) {
    if (!arguments.length) return nodePadding;
    nodePadding = +_;
    return sankey;
  };
 
  sankey.nodes = function(_) {
    if (!arguments.length) return nodes;
    nodes = _;
    return sankey;
  };
 
  sankey.links = function(_) {
    if (!arguments.length) return links;
    links = _;
    return sankey;
  };
 
  sankey.size = function(_) {
    if (!arguments.length) return size;
    size = _;
    return sankey;
  };
 
  sankey.layout = function(iterations) {
    computeNodeLinks();
    computeNodeValues();
    computeNodeBreadths();
    computeNodeDepths(iterations);
    computeLinkDepths();
    return sankey;
  };
 
  sankey.relayout = function() {
    computeLinkDepths();
    return sankey;
  };
 
  sankey.link = function() {
    var curvature = .5;
 
    function link(d) {
      var x0 = d.source.x + d.source.dx,
          x1 = d.target.x,
          xi = d3.interpolateNumber(x0, x1),
          x2 = xi(curvature),
          x3 = xi(1 - curvature),
          y0 = d.source.y + d.sy + d.dy / 2,
          y1 = d.target.y + d.ty + d.dy / 2;
      return "M" + x0 + "," + y0
           + "C" + x2 + "," + y0
           + " " + x3 + "," + y1
           + " " + x1 + "," + y1;
    }
 
    link.curvature = function(_) {
      if (!arguments.length) return curvature;
      curvature = +_;
      return link;
    };
 
    return link;
  };
 
  // Populate the sourceLinks and targetLinks for each node.
  // Also, if the source and target are not objects, assume they are indices.
  function computeNodeLinks() {
    nodes.forEach(function(node) {
      node.sourceLinks = [];
      node.targetLinks = [];
    });
    links.forEach(function(link) {
      var source = link.source,
          target = link.target;
      if (typeof source === "number") source = link.source = nodes[link.source];
      if (typeof target === "number") target = link.target = nodes[link.target];
      source.sourceLinks.push(link);
      target.targetLinks.push(link);
    });
  }
 
  // Compute the value (size) of each node by summing the associated links.
  function computeNodeValues() {
    nodes.forEach(function(node) {
      node.value = Math.max(
        d3.sum(node.sourceLinks, value),
        d3.sum(node.targetLinks, value)
      );
    });
  }
 
  // Iteratively assign the breadth (x-position) for each node.
  // Nodes are assigned the maximum breadth of incoming neighbors plus one;
  // nodes with no incoming links are assigned breadth zero, while
  // nodes with no outgoing links are assigned the maximum breadth.
  function computeNodeBreadths() {
    var remainingNodes = nodes,
        nextNodes,
        x = 0;
 
    while (remainingNodes.length) {
      nextNodes = [];
      remainingNodes.forEach(function(node) {
        node.x = x;
        node.dx = nodeWidth;
        node.sourceLinks.forEach(function(link) {
          nextNodes.push(link.target);
        });
      });
      remainingNodes = nextNodes;
      ++x;
    }
 
    //
    moveSinksRight(x);
    scaleNodeBreadths((size[0] - nodeWidth) / (x - 1));
  }
 
  function moveSourcesRight() {
    nodes.forEach(function(node) {
      if (!node.targetLinks.length) {
        node.x = d3.min(node.sourceLinks, function(d) { return d.target.x; }) - 1;
      }
    });
  }
 
  function moveSinksRight(x) {
    nodes.forEach(function(node) {
      if (!node.sourceLinks.length) {
        node.x = x - 1;
      }
    });
  }
 
  function scaleNodeBreadths(kx) {
    nodes.forEach(function(node) {
      node.x *= kx;
    });
  }
 
  function computeNodeDepths(iterations) {
    var nodesByBreadth = d3.nest()
        .key(function(d) { return d.x; })
        .sortKeys(d3.ascending)
        .entries(nodes)
        .map(function(d) { return d.values; });
 
    //
    initializeNodeDepth();
    resolveCollisions();
    for (var alpha = 1; iterations > 0; --iterations) {
      relaxRightToLeft(alpha *= .99);
      resolveCollisions();
      relaxLeftToRight(alpha);
      resolveCollisions();
    }
 
    function initializeNodeDepth() {
      var ky = d3.min(nodesByBreadth, function(nodes) {
        return (size[1] - (nodes.length - 1) * nodePadding) / d3.sum(nodes, value);
      });
 
      nodesByBreadth.forEach(function(nodes) {
        nodes.forEach(function(node, i) {
          node.y = i;
          node.dy = node.value * ky;
        });
      });
 
      links.forEach(function(link) {
        link.dy = link.value * ky;
      });
    }
 
    function relaxLeftToRight(alpha) {
      nodesByBreadth.forEach(function(nodes, breadth) {
        nodes.forEach(function(node) {
          if (node.targetLinks.length) {
            var y = d3.sum(node.targetLinks, weightedSource) / d3.sum(node.targetLinks, value);
            node.y += (y - center(node)) * alpha;
          }
        });
      });
 
      function weightedSource(link) {
        return center(link.source) * link.value;
      }
    }
 
    function relaxRightToLeft(alpha) {
      nodesByBreadth.slice().reverse().forEach(function(nodes) {
        nodes.forEach(function(node) {
          if (node.sourceLinks.length) {
            var y = d3.sum(node.sourceLinks, weightedTarget) / d3.sum(node.sourceLinks, value);
            node.y += (y - center(node)) * alpha;
          }
        });
      });
 
      function weightedTarget(link) {
        return center(link.target) * link.value;
      }
    }
 
    function resolveCollisions() {
      nodesByBreadth.forEach(function(nodes) {
        var node,
            dy,
            y0 = 0,
            n = nodes.length,
            i;
 
        // Push any overlapping nodes down.
        nodes.sort(ascendingDepth);
        for (i = 0; i < n; ++i) {
          node = nodes[i];
          dy = y0 - node.y;
          if (dy > 0) node.y += dy;
          y0 = node.y + node.dy + nodePadding;
        }
 
        // If the bottommost node goes outside the bounds, push it back up.
        dy = y0 - nodePadding - size[1];
        if (dy > 0) {
          y0 = node.y -= dy;
 
          // Push any overlapping nodes back up.
          for (i = n - 2; i >= 0; --i) {
            node = nodes[i];
            dy = node.y + node.dy + nodePadding - y0;
            if (dy > 0) node.y -= dy;
            y0 = node.y;
          }
        }
      });
    }
 
    function ascendingDepth(a, b) {
      return a.y - b.y;
    }
  }
 
  function computeLinkDepths() {
    nodes.forEach(function(node) {
      node.sourceLinks.sort(ascendingTargetDepth);
      node.targetLinks.sort(ascendingSourceDepth);
    });
    nodes.forEach(function(node) {
      var sy = 0, ty = 0;
      node.sourceLinks.forEach(function(link) {
        link.sy = sy;
        sy += link.dy;
      });
      node.targetLinks.forEach(function(link) {
        link.ty = ty;
        ty += link.dy;
      });
    });
 
    function ascendingSourceDepth(a, b) {
      return a.source.y - b.source.y;
    }
 
    function ascendingTargetDepth(a, b) {
      return a.target.y - b.target.y;
    }
  }
 
  function center(node) {
    return node.y + node.dy / 2;
  }
 
  function value(link) {
    return link.value;
  }
 
  return sankey;
};